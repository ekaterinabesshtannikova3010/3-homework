from typing import List, Dict


def filter_by_state(list_of_dictionaries: List[Dict], state: str = "EXECUTED") -> List[Dict]:
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
    sorted_list = sorted(date_list, key=lambda date_entry: date_entry['date'], reverse=reverse)
    return sorted_list
