# Copyright 2016 Osvaldo Santana Neto
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from datetime import datetime
from typing import List, Union, Optional, Sequence

from PIL import Image as image

from correios import DATADIR
from correios.exceptions import InvalidFederalTaxNumberError, InvalidExtraServiceError, InvalidDirectionError

EXTRA_SERVICE_CODE_SIZE = 2


def _to_integer(number: Union[int, str]) -> int:
    try:
        return int(number.strip())
    except AttributeError:
        return int(number)


def _to_datetime(date: Union[datetime, str], fmt="%Y-%m-%d %H:%M:%S%z") -> datetime:
    if isinstance(date, str):
        last_colon_pos = date.rindex(":")
        date = date[:last_colon_pos] + date[last_colon_pos + 1:]
        return datetime.strptime(date, fmt)
    return date


def _to_federal_tax_number(federal_tax_number) -> "FederalTaxNumber":
    if isinstance(federal_tax_number, FederalTaxNumber):
        return federal_tax_number

    return FederalTaxNumber(federal_tax_number)


def _to_state_tax_number(state_tax_number) -> "StateTaxNumber":
    if isinstance(state_tax_number, StateTaxNumber):
        return state_tax_number

    return StateTaxNumber(state_tax_number)


class AbstractTaxNumber:
    def __init__(self, number: str):
        self._number = self._validate(number)

    @property
    def number(self) -> str:
        return self._number

    def _sanitize(self, raw_number: str) -> str:
        return "".join(d for d in raw_number if d.isdigit())

    def _validate(self, raw_number: str):
        raise NotImplementedError()  # pragma: no cover

    def display(self) -> str:
        raise NotImplementedError()  # pragma: no cover

    def __str__(self):
        return self.number

    def __repr__(self):
        return "<{} number: {}>".format(self.__class__.__name__, self.number)

    def __eq__(self, other):
        return self.number == self._sanitize(other)


class FederalTaxNumber(AbstractTaxNumber):
    FEDERAL_TAX_NUMBER_SIZE = 14

    def _check_verification_digits(self, raw_number):
        number = [int(d) for d in raw_number[:12]]
        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        assert len(number) == len(prod)

        while len(number) < 14:
            r = sum(x * y for (x, y) in zip(number, prod)) % 11
            f = (11 - r) if r > 1 else 0
            number.append(f)
            prod.insert(0, prod[0] + 1)

        number = "".join(str(d) for d in number)
        return raw_number == number

    def _validate(self, raw_number: str):
        raw_number = self._sanitize(raw_number)

        if len(raw_number) != FederalTaxNumber.FEDERAL_TAX_NUMBER_SIZE:
            raise InvalidFederalTaxNumberError(
                "Tax Number must have {} digits".format(self.FEDERAL_TAX_NUMBER_SIZE))

        if not self._check_verification_digits(raw_number):
            raise InvalidFederalTaxNumberError("Invalid Federal Tax Number verification digits")

        return raw_number

    def display(self) -> str:
        return "{}.{}.{}/{}-{}".format(self.number[:2],
                                       self.number[2:5],
                                       self.number[5:8],
                                       self.number[8:12],
                                       self.number[12:])


class StateTaxNumber(AbstractTaxNumber):
    def _validate(self, raw_number: str):
        return self._sanitize(raw_number)

    def display(self) -> str:
        return self.number


class Service:
    # noinspection PyShadowingBuiltins
    def __init__(self,
                 id: int,
                 code: Union[int, str],
                 description: str,
                 category: str,
                 postal_code: Union[int, str],
                 display_name: Optional[str] = "",
                 start_date: Optional[Union[datetime, str]] = None,
                 end_date: Optional[Union[datetime, str]] = None,
                 symbol: Optional[str] = None,
                 default_extra_services: Optional[Sequence[Union["ExtraService", str, int]]] = None):
        self.id = id
        self.code = _to_integer(code)
        self.description = description.strip()
        self.display_name = display_name or self.description
        self.category = category.strip()
        self.postal_code = _to_integer(postal_code)
        self.start_date = _to_datetime(start_date)
        self.end_date = _to_datetime(end_date)
        self.symbol = symbol or "economic"
        self._symbol_image = None

        if default_extra_services is None:
            default_extra_services = []
        self.default_extra_services = [ExtraService.get(es) for es in default_extra_services]

    def __str__(self):
        return str(self.code)

    def get_symbol_filename(self, extension='gif'):
        filename = "{}.{}".format(self.symbol, extension)
        return os.path.join(DATADIR, filename)

    @property
    def symbol_image(self):
        if not self._symbol_image:
            self._symbol_image = image.open(self.get_symbol_filename())
        return self._symbol_image


class ExtraService:
    def __init__(self, number: int, code: str, name: str):
        if not number:
            raise InvalidExtraServiceError("Invalid Extra Service Number {!r}".format(number))
        self.number = number

        if not code or len(code) != EXTRA_SERVICE_CODE_SIZE:
            raise InvalidExtraServiceError("Invalid Extra Service Code {!r}".format(code))
        self.code = code.upper()

        if not name:
            raise InvalidExtraServiceError("Invalid Extra Service Name {!r}".format(name))
        self.name = name

    @classmethod
    def get(cls, service: Union[str, int]):
        if isinstance(service, cls):
            return service

        from .data import EXTRA_SERVICES_LIST
        for extra_service in EXTRA_SERVICES_LIST:
            if extra_service.number == service or extra_service.code == service:
                return extra_service
        else:
            raise InvalidExtraServiceError("Unknown Service {!r}".format(service))

    def __repr__(self):
        return "<ExtraService number={!r}, code={!r}>".format(self.number, self.code)


class Contract:
    def __init__(self,
                 number: Union[int, str],
                 customer_code: int,
                 direction: Union[str, int, 'Direction'],
                 status_code: str,
                 start_date: Union[datetime, str],
                 end_date: Union[datetime, str],
                 posting_cards: Optional[List['PostingCard']] = None):

        self.number = _to_integer(number)
        self.customer_code = customer_code

        if isinstance(direction, str):
            direction = int(direction)

        if isinstance(direction, int):
            direction = Direction.get(direction)

        self.direction = direction

        self.status_code = status_code

        if start_date is not None:
            start_date = _to_datetime(start_date)
        self.start_date = start_date

        if end_date is not None:
            end_date = _to_datetime(end_date)
        self.end_date = end_date

        if posting_cards is None:
            posting_cards = []
        self.posting_cards = posting_cards

    def add_posting_card(self, posting_card: 'PostingCard'):
        self.posting_cards.append(posting_card)

    @property
    def direction_number(self):
        return self.direction.number

    def __str__(self):
        return str(self.number)


class PostingCard:
    ACTIVE = True
    CANCELLED = False

    def __init__(self,
                 contract: Contract,
                 number: Union[int, str],  # 10 digits
                 administrative_code: Union[int, str],  # 8 digits
                 start_date: Union[datetime, str],
                 end_date: Union[datetime, str],
                 status: Union[int, str],  # 2 digits
                 status_code: str,
                 unit: Union[int, str],  # 2 digits
                 services: Optional[List[Service]] = None):
        self.contract = contract
        self._number = _to_integer(number)
        self._administrative_code = _to_integer(administrative_code)
        self.start_date = _to_datetime(start_date)
        self.end_date = _to_datetime(end_date)
        self.status = _to_integer(status)
        self.status_code = status_code
        self.unit = _to_integer(unit)

        if services is None:
            services = []
        self.services = services

        if self not in self.contract.posting_cards:
            self.contract.add_posting_card(self)

    @property
    def number(self):
        return "{:010}".format(self._number)

    @property
    def administrative_code(self):
        return "{:08}".format(self._administrative_code)

    def add_service(self, service: Service):
        self.services.append(service)

    def get_contract_number(self):
        return self.contract.number

    def __repr__(self):
        return "<PostingCard number={!r}, contract={!r}>".format(self.number, self.get_contract_number())

    def __str__(self):
        return self.number


class User:
    def __init__(self,
                 name: str,
                 federal_tax_number: Union[str, FederalTaxNumber],
                 state_tax_number: Optional[Union[str, StateTaxNumber]] = None,
                 status_number: Optional[Union[int, str]] = None,
                 contracts: Optional[List[Contract]] = None):
        self.name = name.strip()
        self.federal_tax_number = _to_federal_tax_number(federal_tax_number)

        if status_number is not None:
            status_number = _to_integer(status_number)
        self.status_number = status_number

        if state_tax_number is not None:
            state_tax_number = _to_state_tax_number(state_tax_number)
        self.state_tax_number = state_tax_number

        if contracts is None:
            contracts = []
        self.contracts = contracts


class Direction:
    def __init__(self, number: int, code: str, name: str):
        if not number:
            raise InvalidDirectionError("Invalid direction number {!r}".format(number))

        if not code:
            raise InvalidDirectionError("Invalid direction code {!r}".format(code))

        if not name:
            raise InvalidDirectionError("Invalid direction name {!r}".format(name))

        self.number = _to_integer(number)
        self.code = code.upper()
        self.name = name

    @classmethod
    def get(cls, search_direction: Union[str, int]):
        if isinstance(search_direction, cls):
            return search_direction

        from .data import DIRECTIONS_LIST
        for direction in DIRECTIONS_LIST:
            if direction.number == search_direction or direction.code == search_direction:
                return direction
        else:
            raise InvalidDirectionError("Unknown direction {!r}".format(search_direction))

    def __repr__(self):
        return "<Direction number={!r}, code={!r}>".format(self.number, self.code)
