###  SKYPRO__coursework3  (версия 1)

#  библиотеки и функции
import json
import os.path

from data.constants import GREEN, NONCOLOR, BLUE, RED, YELLOW
from utils.func import transfer_date, transfer_from_to
from pprint import pprint

##  address
current_file_path = os.path.abspath(__file__)
current_file_dir = os.path.dirname(current_file_path)
data_dir_name = "data"
data_file_name = "operations.json"
data_file_dir = os.path.join(current_file_dir, data_dir_name)
data_file_path = os.path.join(data_file_dir, data_file_name)

# key by task
key_date = "date"  # transfer date key by TS
key_description = "description"  # transfer description key
key_opt = "operationAmount"  # transfer operation key
key_opt_amount = "amount"  # transfer operation amount key
key_opt_crs = "currency"  # transfer operation currency key
key_opt_crs_name = "name"  # transfer operation currency name key


def main():
    with open('data/operations.json', encoding='utf-8') as file:
        list_temp = file.read()
        data_list = json.loads(list_temp)
        data_list_with_date = []
        data_list_without_date = []

        # фильтр на словари с датой и без даты
        for dct in data_list:
            if dct.get(key_date):
                data_list_with_date.append(dct)
            else:
                data_list_without_date.append(dct)

        data_list = sorted(data_list_with_date, key=lambda dt: dt["date"], reverse=True)

    user_number_transaction = int(input("Введите число транзакций для отображения:\n"))
    while user_number_transaction > len(data_list):
        user_number_transaction = int(input(f"В базе хранится информация только о {len(data_list)} транзакциях. "
                                            f"Введите новое число:\n"))

    list_temp = []

    for dct in data_list:
        if dct.get("state") == "EXECUTED":
            if user_number_transaction:
                list_temp.append(dct)
                user_number_transaction -= 1
        else:
            continue

    ##  Вывод информации по запросу пользователя
    for dct in list_temp:
        print(transfer_date(dct), dct.get(key_description, f"{RED}Нет информации{NONCOLOR}"))
        print(transfer_from_to(dct))
        print(dct[key_opt][key_opt_amount], dct[key_opt][key_opt_crs][key_opt_crs_name])
        print()


if __name__ == '__main__':
    main()
