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


def test_empty_list():
    assert get_expenses_by_category([], "food") == []


def test_wrong_category():
    transactions = [
        {"Категория": "shopping", "Дата платежа": "01.01.2022"},
        {"Категория": "entertainment", "Дата платежа": "15.01.2022"},
        {"Категория": "bills", "Дата платежа": "30.01.2022"}
    ]
    assert get_expenses_by_category(transactions, "food") == []


def test_specific_date():
    transactions = [
        {"Категория": "food", "Дата платежа": "01.01.2022"},
        {"Категория": "food", "Дата платежа": "15.01.2022"},
        {"Категория": "food", "Дата платежа": "30.01.2022"}
    ]
    assert get_expenses_by_category(transactions, "food", "15.01.2022") == [
        {"Категория": "food", "Дата платежа": "01.01.2022"},
        {"Категория": "food", "Дата платежа": "15.01.2022"}
    ]


def test_returns_empty_list_if_no_transactions():
    list_normal = [{"Категория": "еда", "Дата платежа": "01.01.2021"},
                   {"Категория": "одежда", "Дата платежа": "02.01.2021"}]
    assert get_expenses_by_category(list_normal, "еда") == []


def test_returns_list():
    list_normal = [{"Категория": "еда", "Дата платежа": "01.01.2022"},
                   {"Категория": "одежда", "Дата платежа": "02.01.2022"}]
    assert isinstance(get_expenses_by_category(list_normal, "еда"), list)
