import unittest
from unittest.mock import patch
from src.reports import get_expenses_by_category

category_word = "Супермаркеты"
test_date = "31.12.2021"


@patch('src.reports.get_expenses_by_category')
def test_get_expenses_with_mock(mock_get_expenses_by_category):
    mock_transactions = [
        {"Категория": "Супермаркеты", "Дата платежа": "31.12.2021", "Сумма операции": 250},
        {"Категория": "Супермаркеты", "Дата платежа": "15.01.2022", "Сумма операции": 200},
    ]
    mock_get_expenses_by_category.return_value = mock_transactions

    expected_result = [
        {"Категория": "Супермаркеты", "Дата платежа": "31.12.2021", "Сумма операции": 250}]
    result = get_expenses_by_category(mock_transactions, category_word, test_date)

    assert result == expected_result, f"Expected {expected_result}, but got {result}"


if __name__ == '__main__':
    unittest.main()
