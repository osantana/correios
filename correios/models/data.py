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


from decimal import Decimal


TRACKING_PREFIX = {
    "AL": "Agentes de leitura",
    "AR": "Avisos de recebimento",
    "AS": "PAC - Ação Social",
    "CA": "Encomenda Internacional - Colis",
    "CB": "Encomenda Internacional - Colis",
    "CC": "Encomenda Internacional - Colis",
    "CD": "Encomenda Internacional - Colis",
    "CE": "Encomenda Internacional - Colis",
    "CF": "Encomenda Internacional - Colis",
    "CG": "Encomenda Internacional - Colis",
    "CH": "Encomenda Internacional - Colis",
    "CI": "Encomenda Internacional - Colis",
    "CJ": "Encomenda Internacional - Colis",
    "CK": "Encomenda Internacional - Colis",
    "CL": "Encomenda Internacional - Colis",
    "CM": "Encomenda Internacional - Colis",
    "CN": "Encomenda Internacional - Colis",
    "CO": "Encomenda Internacional - Colis",
    "CP": "Encomenda Internacional - Colis",
    "CQ": "Encomenda Internacional - Colis",
    "CR": "Carta registrada sem Valor Declarado",
    "CS": "Encomenda Internacional - Colis",
    "CT": "Encomenda Internacional - Colis",
    "CU": "Encomenda internacional - Colis",
    "CV": "Encomenda Internacional - Colis",
    "CW": "Encomenda Internacional - Colis",
    "CX": "Encomenda internacional - Colis ou Selo Lacre para Caixetas",
    "CY": "Encomenda Internacional - Colis",
    "CZ": "Encomenda Internacional - Colis",
    "DA": "SEDEX ou Remessa Expressa com AR Digital",
    "DB": "SEDEX ou Remessa Expressa com AR Digital (Bradesco)",
    "DC": "Remessa Expressa CRLV/CRV/CNH e Notificações",
    "DD": "Devolução de documentos",
    "DE": "Remessa Expressa Talão/Cartão com AR",
    "DF": "e-SEDEX",
    "DG": "SEDEX",
    "DI": "SEDEX ou Remessa Expressa com AR Digital (Itaú)",
    "DJ": "SEDEX",
    "DK": "PAC Extra Grande",
    "DL": "SEDEX",
    "DM": "e-SEDEX",
    "DN": "SEDEX",
    "DO": "SEDEX ou Remessa Expressa com AR Digital (Itaú)",
    "DP": "SEDEX Pagamento na Entrega",
    "DQ": "SEDEX ou Remessa Expressa com AR Digital (Santander)",
    "DR": "Remessa Expressa com AR Digital (Santander)",
    "DS": "SEDEX ou Remessa Expressa com AR Digital (Santander)",
    "DT": "Remessa econômica com AR Digital (DETRAN)",
    "DU": "e-SEDEX",
    "DV": "SEDEX c/ AR digital",
    "DW": "Encomenda SEDEX (Etiqueta Lógica)",
    "DX": "SEDEX 10",
    "EA": "Encomenda Internacional - EMS",
    "EB": "Encomenda Internacional - EMS",
    "EC": "PAC",
    "ED": "Packet Express",
    "EE": "Encomenda Internacional - EMS",
    "EF": "Encomenda Internacional - EMS",
    "EG": "Encomenda Internacional - EMS",
    "EH": "Encomenda Internacional - EMS ou Encomenda com AR Digital",
    "EI": "Encomenda Internacional - EMS",
    "EJ": "Encomenda Internacional - EMS",
    "EK": "Encomenda Internacional - EMS",
    "EL": "Encomenda Internacional - EMS",
    "EM": "Encomenda Internacional - SEDEX Mundi",  # BR Suffix
    # "EM": "Encomenda Internacional - EMS Importação",
    "EN": "Encomenda Internacional - EMS",
    "EO": "Encomenda Internacional - EMS",
    "EP": "Encomenda Internacional - EMS",
    "EQ": "Encomenda de serviço não expressa (ECT)",
    "ER": "Objeto registrado",
    "ES": "e-SEDEX ou EMS",
    "ET": "Encomenda Internacional - EMS",
    "EU": "Encomenda Internacional - EMS",
    "EV": "Encomenda Internacional - EMS",
    "EW": "Encomenda Internacional - EMS",
    "EX": "Encomenda Internacional - EMS",
    "EY": "Encomenda Internacional - EMS",
    "EZ": "Encomenda Internacional - EMS",
    "FA": "FAC registrado",
    "FE": "Encomenda FNDE",
    "FF": "Objeto registrado (DETRAN)",
    "FH": "FAC registrado com AR Digital",
    "FM": "FAC monitorado",
    "FR": "FAC registrado",
    "IA": "Logística Integrada (agendado / avulso)",
    "IC": "Logística Integrada (a cobrar)",
    "ID": "Logística Integrada (devolução de documento)",
    "IE": "Logística Integrada (Especial)",
    "IF": "CPF",
    "II": "Logística Integrada (ECT)",
    "IK": "Logística Integrada com Coleta Simultânea",
    "IM": "Logística Integrada (Medicamentos)",
    "IN": "Correspondência e EMS recebido do Exterior",
    "IP": "Logística Integrada (Programada)",
    "IR": "Impresso Registrado",
    "IS": "Logística integrada standard (medicamentos)",
    "IT": "Remessa Expressa Medicamentos / Logística Integrada Termolábil",
    "IU": "Logística Integrada (urgente)",
    "IX": "EDEI Expresso",
    "JA": "Remessa econômica com AR Digital",
    "JB": "Remessa econômica com AR Digital",
    "JC": "Remessa econômica com AR Digital",
    "JD": "Remessa econômica Talão/Cartão",
    "JE": "Remessa econômica com AR Digital",
    "JF": "Remessa econômica com AR Digital",
    "JG": "Objeto registrado urgente/prioritário",
    "JH": "Objeto registrado urgente / prioritário",
    "JI": "Remessa econômica Talão/Cartão",
    "JJ": "Objeto registrado (Justiça)",
    "JK": "Remessa econômica Talão/Cartão",
    "JL": "Objeto registrado",
    "JM": "Mala Direta Postal Especial",
    "JN": "Objeto registrado econômico",
    "JO": "Objeto registrado urgente",
    "JP": "Receita Federal",
    "JQ": "Remessa econômica com AR Digital",
    "JR": "Objeto registrado urgente / prioritário",
    "JS": "Objeto registrado",
    "JT": "Objeto Registrado Urgente",
    "JV": "Remessa Econômica (c/ AR DIGITAL)",
    "LA": "SEDEX com Logística Reversa Simultânea em Agência",
    "LB": "e-SEDEX com Logística Reversa Simultânea em Agência",
    "LC": "Objeto Internacional (Prime)",
    "LE": "Logística Reversa Econômica",
    "LF": "Objeto Internacional (Prime)",
    "LI": "Objeto Internacional (Prime)",
    "LJ": "Objeto Internacional (Prime)",
    "LK": "Objeto Internacional (Prime)",
    "LM": "Objeto Internacional (Prime)",
    "LN": "Objeto Internacional (Prime)",
    "LP": "PAC com Logística Reversa Simultânea em Agência",
    "LS": "SEDEX Logística Reversa",
    "LV": "Logística Reversa Expressa",
    "LX": "Packet Standard / Econômica",
    "LZ": "Objeto Internacional (Prime)",
    "MA": "Serviços adicionais do Telegrama",
    "MB": "Telegrama (balcão)",
    "MC": "Telegrama (Fonado)",
    "MD": "SEDEX Mundi (Documento interno)",
    "ME": "Telegrama",
    "MF": "Telegrama (Fonado)",
    "MK": "Telegrama (corporativo)",
    "ML": "Fecha Malas (Rabicho)",
    "MM": "Telegrama (Grandes clientes)",
    "MP": "Telegrama (Pré-pago)",
    "MR": "AR digital",
    "MS": "Encomenda Saúde",
    "MT": "Telegrama (Telemail)",
    "MY": "Telegrama internacional (entrante)",
    "MZ": "Telegrama (Correios Online)",
    "NE": "Tele Sena resgatada",
    "NX": "EDEI Econômico (não urgente)",
    "PA": "Passaporte",
    "PB": "PAC",
    "PC": "PAC a Cobrar",
    "PD": "PAC",
    "PE": "PAC",
    "PF": "Passaporte",
    "PG": "PAC",
    "PH": "PAC",
    "PI": "PAC",
    "PJ": "PAC",
    "PK": "PAC Extra Grande",
    "PL": "PAC",
    "PN": "PAC Normal",
    "PR": "Reembolso Postal",
    "QQ": "Objeto de teste (SIGEP Web)",
    "RA": "Objeto registrado / prioritário",
    "RB": "Carta registrada",
    "RC": "Carta registrada com Valor Declarado",
    "RD": "Remessa econômica ou objeto registrado (DETRAN)",
    "RE": "Objeto registrado econômico",
    "RF": "Receita Federal",
    "RG": "Objeto registrado",
    "RH": "Objeto registrado com AR Digital",
    "RI": "Objeto registrado internacional prioritário",
    "RJ": "Objeto registrado",
    "RK": "Objeto registrado",
    "RL": "Objeto registrado",
    "RM": "Objeto registrado urgente",
    "RN": "Objeto registrado (SIGEPWEB ou Agência)",
    "RO": "Objeto registrado",
    "RP": "Reembolso Postal",
    "RQ": "Objeto registrado",
    "RR": "Objeto registrado",
    "RS": "Objeto registrado",
    "RT": "Remessa econômica Talão/Cartão",
    "RU": "Objeto registrado (ECT)",
    "RV": "Remessa econômica CRLV/CRV/CNH e Notificações com AR Digital",
    "RW": "Objeto internacional",
    "RX": "Objeto internacional",
    "RY": "Remessa econômica Talão/Cartão com AR Digital",
    "RZ": "Objeto registrado",
    "SA": "SEDEX",
    "SB": "SEDEX 10",
    "SC": "SEDEX a cobrar",
    "SD": "SEDEX ou Remessa Expressa (DETRAN)",
    "SE": "SEDEX",
    "SF": "SEDEX",
    "SG": "SEDEX",
    "SH": "SEDEX com AR Digital / SEDEX ou AR Digital",
    "SI": "SEDEX",
    "SJ": "SEDEX Hoje",
    "SK": "SEDEX",
    "SL": "SEDEX",
    "SM": "SEDEX 12",
    "SN": "SEDEX",
    "SO": "SEDEX",
    "SP": "SEDEX Pré-franqueado",
    "SQ": "SEDEX",
    "SR": "SEDEX",
    "SS": "SEDEX",
    "ST": "Remessa Expressa Talão/Cartão",
    "SU": "Encomenda de serviço expressa (ECT)",
    "SV": "Remessa Expressa CRLV/CRV/CNH e Notificações com AR Digital",
    "SW": "e-SEDEX",
    "SX": "SEDEX 10",
    "SY": "Remessa Expressa Talão/Cartão com AR Digital",
    "SZ": "SEDEX",
    "TC": "Objeto para treinamento",
    "TE": "Objeto para treinamento",
    "TS": "Objeto para treinamento",
    "VA": "Encomendas com valor declarado",
    "VC": "Encomendas",
    "VD": "Encomendas com valor declarado",
    "VE": "Encomendas",
    "VF": "Encomendas com valor declarado",
    "VV": "Objeto internacional",
    "XA": "Aviso de chegada (internacional)",
    "XM": "SEDEX Mundi",
    "XR": "Encomenda SUR Postal Expresso",
    "XX": "Encomenda SUR Postal 24 horas",
}

EXTRA_SERVICES = {
    1: {'code': "AR", 'name': "Aviso de Recebimento"},
    2: {'code': "MP", 'name': "Mão Própria Nacional"},
    19: {'code': "VD", 'name': "Valor Declarado (Encomendas)"},
    25: {'code': "RR", 'name': "Registro Nacional"},
}

EXTRA_SERVICE_AR = 1
EXTRA_SERVICE_MP = 2
EXTRA_SERVICE_VD = 19
EXTRA_SERVICE_RR = 25

SERVICES = {
    40215: {
        'id': 104707,
        'description': 'SEDEX 10',
        'category': 'SERVICO_COM_RESTRICAO',
        'max_weight': 10000,
        'display_name': 'SEDEX 10',
        'symbol': "premium",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    81019: {
        'id': 104672,
        'description': 'E-SEDEX STANDARD',
        'category': 'SERVICO_COM_RESTRICAO',
        'max_weight': 15000,
        'display_name': 'E-SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    41068: {
        'id': 109819,
        'description': 'PAC',
        'category': 'PAC',
        'display_name': 'PAC',
        'max_weight': 30000,
        'symbol': "standard",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("3000.00"),
    },
    40444: {
        'id': 109811,
        'description': 'SEDEX - CONTRATO',
        'category': 'SEDEX',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    40436: {
        'id': 109810,
        'description': 'SEDEX - CONTRATO',
        'category': 'SEDEX',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    40096: {
        'id': 104625,
        'description': 'SEDEX (CONTRATO)',
        'category': 'SEDEX',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    40380: {
        'id': 109806,
        'description': 'SEDEX REVERSO 40096',
        'category': 'REVERSO',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    40010: {
        'id': 104295,
        'description': 'SEDEX A VISTA',
        'category': 'SEDEX',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    41211: {
        'id': 113546,
        'description': 'PAC - CONTRATO',
        'category': 'PAC',
        'display_name': 'PAC',
        'max_weight': 30000,
        'symbol': "standard",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("3000.00"),
    },
    40630: {
        'id': 114976,
        'description': 'SEDEX PAGAMENTO NA ENTREGA -',
        'category': 'SEDEX',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    40916: {
        'id': 118568,
        'description': 'SEDEX AGRUPADO II',
        'category': 'SEDEX',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    40908: {
        'id': 118567,
        'description': 'SEDEX AGRUPADO I',
        'category': 'SEDEX',
        'max_weight': 30000,
        'display_name': 'SEDEX',
        'symbol': "express",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    41300: {
        'id': 120366,
        'description': 'PAC GRANDES FORMATOS',
        'category': 'SERVICO_COM_RESTRICAO',
        'max_weight': 50000,
        'display_name': 'PAC',
        'symbol': "standard",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("3000.00"),
    },
    40169: {
        'id': 115218,
        'description': 'SEDEX 12',
        'category': 'SERVICO_COM_RESTRICAO',
        'max_weight': 10000,
        'display_name': 'SEDEX 12',
        'symbol': "premium",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    40290: {
        'id': 108934,
        'description': 'SEDEX HOJE',
        'category': 'SERVICO_COM_RESTRICAO',
        'max_weight': 10000,
        'display_name': 'SEDEX Hoje',
        'symbol': "premium",
        'default_extra_services': [EXTRA_SERVICE_RR],
        'min_declared_value': Decimal("17.00"),
        'max_declared_value': Decimal("10000.00"),
    },
    10154: {
        'id': 118424,
        'description': 'CARTA COMERCIAL  REGISTRADA',
        'category': 'CARTA_REGISTRADA',
        'display_name': 'Carta Registrada',
    },
    41246: {
        'id': 115487,
        'description': 'REM. CAMPANHA PAPAI NOEL DOS',
        'category': 'SEM_CATEGORIA',
        'display_name': 'Papai Noel dos Correios'},
    40150: {
        'id': 115136,
        'description': 'SERVICO DE PROTOCOLO POSTAL -',
        'category': 'SEDEX',
        'display_name': 'Protocolo',
    },
    10065: {
        'id': 109480,
        'description': 'CARTA COMERCIAL A FATURAR',
        'category': 'CARTA_REGISTRADA',
        'display_name': 'Carta Comercial',
    }
}

SERVICE_PAC = 41068
SERVICE_SEDEX = 40096
SERVICE_SEDEX10 = 40215
SERVICE_SEDEX12 = 40169
SERVICE_E_SEDEX = 81019

REGIONAL_DIRECTIONS = {
    1: {'code': "AC", 'name': "AC - ADMINISTRAÇAO CENTRAL"},
    3: {'code': "ACR", 'name': "DR - ACRE"},
    4: {'code': "AL", 'name': "DR - ALAGOAS"},
    6: {'code': "AM", 'name': "DR - AMAZONAS"},
    5: {'code': "AP", 'name': "DR - AMAPÁ"},
    8: {'code': "BA", 'name': "DR - BAHIA"},
    10: {'code': "BSB", 'name': "DR - BRASÍLIA"},
    12: {'code': "CE", 'name': "DR - CEARÁ"},
    14: {'code': "ES", 'name': "DR - ESPIRITO SANTO"},
    16: {'code': "GO", 'name': "DR - GOIÁS"},
    18: {'code': "MA", 'name': "DR - MARANHÃO"},
    20: {'code': "MG", 'name': "DR - MINAS GERAIS"},
    22: {'code': "MS", 'name': "DR - MATO GROSSO DO SUL"},
    24: {'code': "MT", 'name': "DR - MATO GROSSO"},
    28: {'code': "PA", 'name': "DR - PARÁ"},
    30: {'code': "PB", 'name': "DR - PARAÍBA"},
    32: {'code': "PE", 'name': "DR - PERNAMBUCO"},
    34: {'code': "PI", 'name': "DR - PIAUÍ"},
    36: {'code': "PR", 'name': "DR - PARANÁ"},
    50: {'code': "RJ", 'name': "DR - RIO DE JANEIRO"},
    60: {'code': "RN", 'name': "DR - RIO GRANDE DO NORTE"},
    26: {'code': "RO", 'name': "DR - RONDONIA"},
    65: {'code': "RR", 'name': "DR - RORAIMA"},
    64: {'code': "RS", 'name': "DR - RIO GRANDE DO SUL"},
    68: {'code': "SC", 'name': "DR - SANTA CATARINA"},
    70: {'code': "SE", 'name': "DR - SERGIPE"},
    74: {'code': "SPI", 'name': "DR - SÃO PAULO INTERIOR"},
    72: {'code': "SPM", 'name': "DR - SÃO PAULO"},
    75: {'code': "TO", 'name': "DR - TOCANTINS"},
}

TRACKING_EVENT_TYPES = {
    "ERROR": "Evento de erro",  # custom event type for "Not Found" error
    "BDE": "Baixa de distribuição externa",
    "BDI": "Baixa de distribuição interna",
    "BDR": "Baixa corretiva",
    "BLQ": "Bloqueio de objetos",
    "CAR": "Conferência de lista de registro",
    "CD": "Conferência de nota de despacho",
    "CMT": "Chegada de um meio de transporte",
    "CO": "Coleta de objetos",
    "CUN": "Conferência de lista de registro",
    "DO": "Expedição de nota de despacho",
    "EST": "Estorno",
    "FC": "Função complementar",
    "IDC": "Indenização de objetos",
    "LDI": "Lista de distribuição interna",
    "LDE": "Lista de distribuição externa",
    "OEC": "Lista de Objetos Entregues ao Carteiro",
    "PAR": "Conferência Unidade Internacional",
    "PMT": "Partida Meio de Transporte",
    "PO": "Postagem (exceção)",
    "RO": "Expedição de Lista de Registro",
    "TRI": "Triagem",
    "CMR": "Evento Desconhecido",
}
