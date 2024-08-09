import unittest
from unittest.mock import patch
import pandas as pd
from pathlib import Path
from src.utils import top_transaction, current_time, card_information, fetch_stock_prices, get_currency_rates
import datetime
import pytest

ROOTPATH = "path/to/your/project"
file_xlsx = "transactions.xlsx"


def test_top_transaction():
    list_transactions = [
        {'Дата операции': '2019-03-21', 'Сумма платежа': 190044.51, 'Категория': 'Переводы',
         'Описание': 'Перевод Кредитная карта. ТП 10.2 RUR'},
        {'Дата операции': '2018-10-23', 'Сумма платежа': 177506.03, 'Категория': 'Переводы',
         'Описание': 'Перевод Кредитная карта. ТП 10.2 RUR'},
        {'Дата операции': '2021-12-30', 'Сумма платежа': 174000.0, 'Категория': 'Пополнения',
         'Описание': 'Пополнение через Газпромбанк'},
        {'Дата операции': '2021-09-14', 'Сумма платежа': 150000.0, 'Категория': 'Пополнения',
         'Описание': 'Перевод с карты'},
        {'Дата операции': '2020-07-31', 'Сумма платежа': 150000.0, 'Категория': 'Пополнения',
         'Описание': 'Перевод с карты'}
    ]

    expected_result = {'top_transactions': [
        {'date': '21.03.2019 17:01:38', 'amount': 190044.51, 'category': 'Переводы',
         'description': 'Перевод Кредитная карта. ТП 10.2 RUR'},
        {'date': '23.10.2018 12:26:15', 'amount': 177506.03, 'category': 'Переводы',
         'description': 'Перевод Кредитная карта. ТП 10.2 RUR'},
        {'date': '30.12.2021 17:50:17', 'amount': 174000.0, 'category': 'Пополнения',
         'description': 'Пополнение через Газпромбанк'},
        {'date': '14.09.2021 14:57:42', 'amount': 150000.0, 'category': 'Пополнения',
         'description': 'Перевод с карты'},
        {'date': '31.07.2020 22:27:45', 'amount': 150000.0, 'category': 'Пополнения',
         'description': 'Перевод с карты'}]}

    with patch('builtins.sorted', side_effect=Exception('Test exception')):
        result = top_transaction(list_transactions)


def test_empty_list():
    """Тест на пустой список транзакций"""
    result = top_transaction([])
    assert result == {"top_transactions": []}, "Ошибка: Должен быть пустой список транзакций"


def test_incomplete_transactions():
    """Тест на список транзакций с отсутствующими полями"""
    list_transactions = [
        {'Дата операции': '2024-07-01', 'Сумма платежа': 100, 'Категория': 'Еда'},
        {'Дата операции': '2024-07-02', 'Сумма платежа': 200, 'Категория': 'Транспорт', 'Описание': 'Такси'},
        {'Дата операции': '2024-07-03', 'Сумма платежа': 150, 'Категория': 'Развлечения', 'Описание': 'Кино'},
    ]
    result = top_transaction(list_transactions)
    assert len(result["top_transactions"]) <= 5, "Ошибка: Должно быть не более 5 транзакций"
    assert all(
        'Описание' in t for t in result["top_transactions"]), "Ошибка: Все транзакции должны иметь поле 'Описание'"


def processing_transaction():
    """Функция для обработки Еxcel файла."""
    try:
        df_excel = pd.read_excel(Path(ROOTPATH, file_xlsx), engine="openpyxl")
        list_dict = df_excel.to_dict(orient="records")
        return list_dict
    except Exception as e:
        return []


@patch('pandas.read_excel')
def test_processing_transaction_with_mock(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([])

    result = processing_transaction()
    assert result == []

    mock_read_excel.assert_called_once_with(Path(ROOTPATH, file_xlsx), engine="openpyxl")


if __name__ == '__main__':
    unittest.main()


def test_current_time():
    fixed_time = datetime.datetime(2023, 10, 1, 15, 30, 45)

    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = fixed_time
        result = current_time()

        assert result == "15:30:45"


def test_empty_list():
    empty_list = []
    assert card_information(empty_list) == {"cards": []}


def test_fetch_stock_prices_empty_symbols():
    symbols = []
    api_key = "your_api_key_here"

    result = fetch_stock_prices(symbols, api_key)

    assert result == []


def test_get_currency_rates():
    api_key = "your_api_key"
    expected_currencies = ["EUR", "USD", "GBP", "RUB"]
    currency_rates = get_currency_rates(api_key)
    assert isinstance(currency_rates, list)
    for currency_rate in currency_rates:
        assert isinstance(currency_rate, dict)
        assert "currency" in currency_rate
        assert "rate" in currency_rate
        assert currency_rate["currency"] in expected_currencies


def test_empty_api_key():
    assert get_currency_rates("") == []


def test_single_transaction():
    transactions = [{"Номер карты": "1234567812345678", "Сумма операции": 1500}]
    assert card_information(transactions) == {"cards": [{"last_digits": "1234567812345678",
                                                         "total_spent": 1500, "cashback": 15}]}


def test_card_information_single_transaction():
    transactions = [{'Номер карты': '1234', 'Сумма операции': 500}]
    assert card_information(transactions) == {"cards": [{"last_digits": '1234', "total_spent": 500, "cashback": 5}]}


def test_top_transaction_empty_list():
    assert top_transaction([]) == {"top_transactions": []}


def test_top_transaction_single_transaction():
    transactions = [
        {"Дата операции": "2024-08-08", "Сумма платежа": 100, "Категория": "Groceries",
         "Описание": "Grocery shopping"}]
    assert top_transaction(transactions) == {"top_transactions": [
        {"date": "2024-08-08", "amount": 100, "category": "Groceries", "description": "Grocery shopping"}]}


def test_current_time_invalid_time_handling():
    """Проверка на возврат значения, если произошла ошибка."""
    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.side_effect = Exception("Ошибка получения времени")
        assert current_time() == "00:00:00"


def test_invalid_api_key():
    api_key = "invalid_api_key"
    result = get_currency_rates(api_key)
    assert result == []


def test_fetch_stock_prices_invalid_api_key():
    symbols = ["AAPL"]
    response = fetch_stock_prices(symbols, "")
    msg = 'Invalid API key'
    for r in response:
        if r['stock'] is not None and r['price'] is not None:
            raise Exception(msg)


if __name__ == "__main__":
    pytest.main()
