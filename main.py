# from src.config import ROOTPATH
# from pathlib import Path
from src.processing import filter_by_state, sort_by_date, format_transaction
import pandas as pd
from src.user import choice_status
from src.transactions import count_operations_by_category


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = ""

    while choice not in ("1", "2", "3"):
        choice = input()
        if choice not in ("1", "2", "3"):
            print("Выберите доступные варианты 1, 2 или 3.Пользователь: ")
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        file_main = "data/operations.json"
        json_data = pd.read_json(file_main)
        transact = json_data.to_dict('records')
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        file_main = "C:data/transactions.csv"
        csv_data = pd.read_csv(file_main, delimiter=";")
        csv_data["operationAmount"] = csv_data.apply(lambda row:
                                                 {"amount": row["amount"], "currensy": {"name": row["currency_name"],
                                                                                        "code": row["currency_code"]}},
                                                 axis=1)

        new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
        csv_data = csv_data[new_col_order]
        transact = csv_data.to_dict('records')
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        file_main = "data/transactions_excel.xlsx"
        excel_data = pd.read_excel(file_main)
        excel_data["operationAmount"] = excel_data.apply(lambda row:
                                                     {"amount": row["amount"],
                                                      "currensy": {"name": row["currency_name"],
                                                                   "code": row["currency_code"]}},
                                                     axis=1)

        new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
        excel_data = excel_data[new_col_order]
        transact = excel_data.to_dict('records')

    user_status = choice_status().upper()

    transactions_sorted = filter_by_state(transact, user_status)

    print(f"Операции отфильтрованы по статусу {user_status}")
    print()

    sort_date = ""
    sort_order = ""

    while sort_date not in ["ДА", "НЕТ"]:
        sort_date = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").upper()
        if sort_date not in ("ДА", "НЕТ"):
            print(f'Вариант "{sort_date}" недоступен.')
    if sort_date == "ДА":
        print("Выбран вариант ДА")
        while sort_order not in ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"]:
            sort_order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").upper()
            if sort_order not in ("ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"):
                print(f'Вариант "{sort_order}" недоступен.')
        if sort_order == "ПО ВОЗРАСТАНИЮ":
            print("Выбран вариант ПО  ВОЗРАСТАНИЮ")
            transactions_sorted = sort_by_date(transactions_sorted, reverse=False)
        elif sort_order == "ПО УБЫВАНИЮ":
            print("Выбран вариант ПО УБЫВАНИЮ")
            transactions_sorted = sort_by_date(transactions_sorted)
        else:
            print("Ошибка ввода! Попробуйте ещё раз.")
    elif sort_date == "НЕТ":
        print("Выбран вариант НЕТ")
    else:
        print("Ошибка ввода! Попробуйте ещё раз.")

    sort_rub = ""

    while sort_rub not in ["ДА", "НЕТ"]:
        sort_rub = input("Выводит только рублевые тразакции? Да / Нет\nПользователь: ").upper()
        if sort_rub not in ("ДА", "НЕТ"):
            print(f'Вариант "{sort_rub}" недоступен.')
    if sort_rub == "ДА":
        print("Выбран вариант ДА")
        print(transactions_sorted)
        transactions_sorted = [transaction for transaction in transactions_sorted if
                               transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == "RUB"]
    elif sort_rub == "НЕТ":
        print("Выбран вариант НЕТ")
    else:
        print("Ошибка ввода! Попробуйте ещё раз.")

    sort_word = ""

    while sort_word not in ["ДА", "НЕТ"]:
        sort_word = input("Отфильтровать список транзакций по определенному слову в описании? ДА/НЕТ\n"
                          "Пользователь: ").upper()
        if sort_word not in ("ДА", "НЕТ"):
            print(f'Вариант "{sort_word}" недоступен.')
    if sort_word == "ДА":
        print("Выбран вариант ДА")
        word = input("Введите слово: ")
        # print(transactions_sorted)
        filtered_list = [d for d in transactions_sorted if "description" in d and word in d["description"]]
    elif sort_word == "НЕТ":
        print("Выбран вариант НЕТ")
        transactions_sorted = description_transactions(transactions_sorted)
    else:
        print("Такого слова нет.")

    print("Распечатываю итоговый список транзакций...")
    print(filtered_list)

    if len(filtered_list) > 0:
         print(f"Всего банковских операций ввыборке: {len(filtered_list)}\n")

    #      for transaction in filtered_list:
    #        print(format_transaction(transaction))
    # else:
    #     print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

main()
