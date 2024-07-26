import unittest
from unittest.mock import patch
from src.services import normalize_transactions

@patch('src.services.normalize_transactions')
def test_normalize_transactions():
    mock_transactions = [
        {"Описание": 123, "Категория": 456, "Номер карты": "1234", "Сумма операции": 100.0},
        {"Описание": None, "Категория": "Покупки", "Номер карты": "5678", "Сумма операции": 50.0},
        {"Описание": "Кафе", "Категория": None, "Номер карты": "9012", "Сумма операции": 75.0}
    ]

    result = normalize_transactions(mock_transactions)
    expected_result = [
        {"Описание": "123", "Категория": "456", "Номер карты": "1234", "Сумма операции": 100.0},
        {"Описание": "", "Категория": "Покупки", "Номер карты": "5678", "Сумма операции": 50.0},
        {"Описание": "Кафе", "Категория": "", "Номер карты": "9012", "Сумма операции": 75.0}
    ]
    assert result == expected_result


@patch('src.views.list_transactions')
def test_card_information(mock_list_transactions):
    mock_list_transactions = {'cards': []}
    expected_result = {'cards': []}
    result = card_information()
    assert result == expected_result



if __name__ == '__main__':
    test_normalize_transactions()