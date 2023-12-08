from datetime import datetime
from data.constants import YELLOW, NONCOLOR, GREEN, RED, BLUE


def transfer_date(d: dict) -> str:
    """
    Pulls out the date of the transaction and shows it in the desired format.
    :param d: dictionary with transaction
    :return: date in the format DD.MM.YYYY
    """
    key_date = "date"  # transfer date key

    if key_date in d:
        date_str = d[key_date][:10]
        date_format = '%Y-%m-%d'
        date_format_new = '%d.%m.%Y'

        date = datetime.strptime(date_str, date_format).strftime(date_format_new)

        return f"{YELLOW}{date}{NONCOLOR}"
    else:
        return f"{RED}Нет информации по дате транзакции{NONCOLOR}"


def transfer_from_to(d: dict) -> str:
    """
    Вытаскивает из транзакции информацию по счетам откуда / куда.
    :param d: словарь с транзакцией
    :return: откуда -> куда (в нужном формате)
    """
    key_from = "from"  # transfer from key
    key_to = "to"  # transfer to key

    if key_from in d:
        list_from = d[key_from].split()
        ac_from = list_from[1]
        value_from = f'{list_from[0]} {GREEN}{ac_from[:4]} {ac_from[4:6]}** **** {ac_from[-4:]}{NONCOLOR}'
    else:
        value_from = f"{RED}Точка входа в транзакцию неизвестна{NONCOLOR}"

    if key_to in d:
        list_to = d[key_to].split()
        value_to = f"{list_to[0]} {BLUE}**{list_to[1][-4:]}{NONCOLOR}"
    else:
        value_to = f"{RED}Точка выхода из транзакции неизвестна{NONCOLOR}"

    return f"{value_from} -> {value_to}"
