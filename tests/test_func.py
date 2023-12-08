from data.constants import GREEN, NONCOLOR, BLUE, RED, YELLOW
from utils.func import transfer_from_to, transfer_date

dct1 = {'id': 441945886,
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041',
        'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод организации',
        'from': 'Maestro 1596837868705199',
        'to': 'Счет 64686473678894779589',
        }
dct2 = {'id': 441945886,
        'state': 'EXECUTED',
        'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод организации',
        'to': 'Счет 64686473678894779589',
        }
dct3 = {'id': 441945886,
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041',
        'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Перевод организации',
        'from': 'Maestro 1596837868705199',
        }


def test_transfer_date():
    t11 = f"{transfer_date(dct1)}"
    t12 = f"{YELLOW}26.08.2019{NONCOLOR}"
    assert t11 == t12

    t21 = f"{transfer_date(dct2)}"
    t22 = f"{RED}Нет информации по дате транзакции{NONCOLOR}"
    assert t21 == t22


def test_transfer_from_to():
    t11 = f"{transfer_from_to(dct1)}"
    t12 = f"Maestro {GREEN}1596 83** **** 5199{NONCOLOR} -> Счет {BLUE}**9589{NONCOLOR}"
    assert t11 == t12

    t21 = f"{transfer_from_to(dct2)}"
    t22 = f"{RED}Точка входа в транзакцию неизвестна{NONCOLOR} -> Счет {BLUE}**9589{NONCOLOR}"
    assert t21 == t22

    t31 = f"{transfer_from_to(dct3)}"
    t32 = f"Maestro {GREEN}1596 83** **** 5199{NONCOLOR} -> {RED}Точка выхода из транзакции неизвестна{NONCOLOR}"
    assert t31 == t32
