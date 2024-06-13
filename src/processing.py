from typing import List, Dict

def filter_by_state(list_of_dictionaries: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция для поиска словарей с конкреным значением ключа.
    """
    returned_list = []
    for i in list_of_dictionaries:
        if i["state"] == state:
            returned_list.append(i)
    return returned_list


