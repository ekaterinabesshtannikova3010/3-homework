from unittest.mock import patch
from src.services import search_transactions


def test_search_transactions_with_mock():
    # Создаем тестовые данные
    normal_transactions = [
        {"Описание": "Покупка в магазине красоты", "Категория": "Красота"},
        {"Описание": "Обед в кафе", "Категория": "Питание"},
        {"Описание": "Поход в кино", "Категория": "Развлечения"},
        {"Описание": "Покупка косметики", "Категория": "Красота"},
    ]

    # Патчим функцию input(), чтобы вернуть тестовый запрос
    with patch('builtins.input', return_value='Красота'):
        # Вызываем функцию search_transactions() с тестовыми данными
        result = search_transactions(normal_transactions)

    # Проверяем, что функция вернула ожидаемый результат
    expected_result = [
        {"Описание": "Покупка в магазине красоты", "Категория": "Красота"},
        {"Описание": "Покупка косметики", "Категория": "Красота"},
    ]
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    # Проверяем, что логирование было вызвано
    with patch('logging.info') as mock_log_info:
        search_transactions(normal_transactions)
        mock_log_info.assert_called_once_with("Search by query: 'Красота'. Found 2 transactions.")


if __name__ == '__main__':
    test_search_transactions_with_mock()
