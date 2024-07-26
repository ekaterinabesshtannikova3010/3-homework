import unittest
from unittest import mock
from pathlib import Path
import pandas as pd
from src.views import top_transaction, card_information
from unittest.mock import patch


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
        {'date': '14.09.2021 14:57:42', 'amount': 150000.0, 'category': 'Пополнения', 'description': 'Перевод с карты'},
        {'date': '31.07.2020 22:27:45', 'amount': 150000.0, 'category': 'Пополнения',
         'description': 'Перевод с карты'}]}

    with patch('builtins.sorted', side_effect=Exception('Test exception')):
        result = top_transaction(list_transactions)


if __name__ == '__main__':
    unittest.main()


@patch('src.views.list_transactions')
def test_card_information(mock_list_transactions):
    mock_list_transactions = {'cards': []}
    expected_result = {'cards': []}
    result = card_information()
    assert result == expected_result


if __name__ == '__main__':
    unittest.main()
