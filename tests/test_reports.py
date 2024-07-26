import datetime
import logging
from unittest.mock import patch
from src.reports import get_expenses_by_category


#
# @patch('src.views.total_expenses')
# def test_get_expenses(mock_total_expenses):
#     transactions = []
#     expected_result = []
#     result == get_expenses_by_category
#     assert result == expected_result
#
# if __name__ == '__main__':
#     unittest.main()
#
def test_get_expenses_with_mock():
    transactions = [
        {"Категория": "Супермаркеты", "Дата платежа": "01.12.2021", "Сумма операции": 100},
        {"Категория": "Супермаркеты", "Дата платежа": "15.01.2022", "Сумма операции": 200},
        {"Категория": "Развлечения", "Дата платежа": "20.12.2021", "Сумма операции": 150},
        {"Категория": "Супермаркеты", "Дата платежа": "30.12.2021", "Сумма операции": 250},
        {"Категория": "Супермаркеты", "Дата платежа": "15.11.2021", "Сумма операции": 300},
    ]


category_word = "Супермаркеты"
test_date = "31.12.2021"

result = get_expenses_by_category(transactions, category_word, test_date)

expected_result = [
    {"Категория": "Супермаркеты", "Дата платежа": "15.01.2022", "Сумма операции": 200},
    {"Категория": "Супермаркеты", "Дата платежа": "31.12.2021", "Сумма операции": 250},
]

# Проверка результата
assert result == expected_result, f"Expected {expected_result}, but got {result}"
if __name__ == '__main__':
    unittest.main()
