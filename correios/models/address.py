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


from typing import List, TypeVar, Union

from decimal import Decimal
from phonenumbers import PhoneNumberFormat, parse, format_number

from correios.exceptions import InvalidZipCodeException, InvalidStateException

ZIP_CODE_LENGTH = 8
STATE_LENGTH = 2


class ZipCode(object):
    def __init__(self, code: str):
        self._code = self._validate(code)

    @property
    def code(self) -> str:
        return self._code

    def _validate(self, code) -> str:
        code = "".join(d for d in code if d.isdigit())

        if len(code) != ZIP_CODE_LENGTH:
            raise InvalidZipCodeException("ZipCode code must have 8 digits")

        return code

    def display(self) -> str:
        return "{}-{}".format(self.code[:5], self.code[-3:])

    def __eq__(self, other):
        return self._code == self._validate(other)

    def __str__(self):
        return self.code

    def __repr__(self):
        return "<ZipCode code: {}>".format(self.code)


class State(object):
    STATES = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins',
    }
    _name_map = {v.lower(): k for k, v in STATES.items()}

    def __init__(self, code: str):
        self._code = self._validate(code)

    @property
    def code(self) -> str:
        return self._code

    def _validate(self, raw_state) -> str:
        state = self._name_map.get(raw_state.lower(), raw_state)
        state = state.upper()

        if len(state) != STATE_LENGTH or state not in self.STATES:
            raise InvalidStateException("State code {} is invalid".format(state))

        return state

    def display(self):
        return self.STATES[self.code]

    def __eq__(self, other):
        return self.code == self._validate(other)

    def __str__(self):
        return self.code

    def __repr__(self):
        return "<State code: {} name: {}>".format(self.code, self.display())


StateType = TypeVar("StateType", State, str)


class ZipAddress(object):
    # noinspection PyShadowingBuiltins
    def __init__(self,
                 id: int,
                 zip_code: Union[ZipCode, str],
                 state: StateType,
                 city: str,
                 district: str,
                 address: str,
                 complements: List[str]):
        self.id = id
        self.zip_code = ZipCode(str(zip_code))
        self.state = State(str(state))
        self.city = city
        self.district = district
        self.address = address
        self.complements = [c for c in complements if c]


class Phone(object):
    def __init__(self, number: str, country="BR"):
        self.parsed = self._parse(number, country)
        self.country = country
        self.number = "".join(d for d in number if d.isdigit())

    def _parse(self, number: str, country: str):
        if number.startswith("+"):
            return parse(number)
        return parse(number, country)

    def display(self) -> str:
        return format_number(self.parsed, PhoneNumberFormat.INTERNATIONAL)

    def __eq__(self, other: Union["Phone", str]):
        if isinstance(other, Phone):
            return self.parsed == other.parsed
        other = self._parse(other, self.country)
        return self.parsed == other

    def __str__(self):
        return "{}{}".format(self.parsed.country_code, self.parsed.national_number)

    def __repr__(self):
        return "<Phone {!s}>".format(self)


class Address(object):
    def __init__(self,
                 name: str,
                 street: str,
                 number: str,
                 city: str,
                 state: Union[State, str],
                 zip_code: Union[ZipCode, str],
                 complement: str = "",
                 neighborhood: str = "",
                 phone: Union[Phone, str] = "",
                 cellphone: Union[Phone, str] = "",
                 email: str = "",
                 latitude: Union[Decimal, str] = "0.0",
                 longitude: Union[Decimal, str] = "0.0",
                 ):
        self.name = name
        self.street = street
        self.number = number
        self.city = city
        self.complement = complement
        self.neighborhood = neighborhood
        self.email = email

        if not isinstance(state, State):
            state = State(state)
        self.state = state

        if not isinstance(zip_code, ZipCode):
            zip_code = ZipCode(zip_code)
        self.zip_code = zip_code

        if phone and not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phone = phone

        if cellphone and not isinstance(cellphone, Phone):
            cellphone = Phone(cellphone)
        self.cellphone = cellphone

        if not isinstance(latitude, Decimal):
            latitude = Decimal(latitude)
        self.latitude = latitude

        if not isinstance(longitude, Decimal):
            longitude = Decimal(longitude)
        self.longitude = longitude
