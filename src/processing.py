from typing import Dict, List
from dateutil.parser import parse
from src.utils import process_transaction

def filter_by_state(list_of_dictionaries: List[Dict], state: str ="EXECUTED") -> List[Dict]:
    """
    Функция для поиска словарей с конкреным значением ключа.
    """
    returned_list = []
    for lis in list_of_dictionaries:
        if lis["state"] == state:
            returned_list.append(lis)
    return returned_list


def sort_by_date(date_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция для сортировки словарей по убыванию."""
    sorted_list = sorted(date_list, key=lambda date_entry: date_entry["date"], reverse=reverse)
    return sorted_list
#
# list_from_csv = process_transaction()
# transaction  = list_from_csv
def format_transaction(transaction):
    """Форматирование финального вывода в консоль"""
    date_str = transaction.get("date", "N/A")
    if date_str != "N/A":
        date_str = parse(date_str).strftime("%d.%m.%Y")

    description = transaction.get("description", "N/A")

    amount_info = transaction.get("operationAmount", {})
    amount = amount_info.get("amount", "N/A")
    if isinstance(amount, str) and amount.replace(".", "").isdigit():
        amount = float(amount)
        amount = round(amount)
    elif isinstance(amount, float) and not math.isnan(amount):
        amount = round(amount)
    else:
        amount = "N/A"

    currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "N/A")

    from_field = transaction.get("from", {})
    to_field = transaction["to"]
    from_account = mask_account_card(from_field)
    to_account = mask_account_card(to_field)
    from_card = mask_account_card(from_field)
    to_card = mask_account_card(to_field)

    if transaction["description"] == "Перевод с карты на карту":

        return f"{date_str} {description}\n{from_card} -> {to_card}\nСумма: {amount} {currency}\n"

    elif transaction["description"] == "Перевод со счета на счет":

        return f"{date_str} {description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n"

    elif transaction["description"] == "Перевод организации":

        return f"{date_str} {description}\n{from_card} -> {to_account}\nСумма: {amount} {currency}\n"

    elif transaction["description"] == "Открытие вклада":

        return f"{date_str} {description}\n{to_account}\nСумма: {amount} {currency}\n"

    else:

        return f"{date_str} {description}\nСчет {to_account}\nСумма: {amount} {currency}\n"

# print(format_transaction(transaction))
if __name__ == "__main__":
    print(list_from_csv)
    for transaction in list_from_csv:
        print(format_transaction(transaction))