from src.processing import filter_by_state


def test_filter_by_state(test_list):
    """
    Тестирование функции для поиска словарей с значением ключа по умолчанию.
    """
    assert filter_by_state(test_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_empty():
    """
    Тестирование функции на пустой словарь.
    """
    assert filter_by_state([]) == []
