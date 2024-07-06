import pytest
import json
import requests
import os

from pathlib import Path
from src.external_api import convert_transaction_to_rubles
from unittest.mock import Mock, patch


@patch("requests.get")
def test_convert_transaction_to_rubles(mock_get):
    mock_get.return_value.json.return_value = {"result": 1}
    assert convert_transaction_to_rubles({'id': 441945886,
                                          "state": "EXECUTED",
                                          "date": "2019-08-26T10:50:58.294041",
                                          "operationAmount": {
                                              "amount": "1",
                                              "currency": {
                                                  "name": "руб.",
                                                  "code": "RUB"
                                              }
                                          },
                                          "description": "Перевод организации",
                                          "from": "Maestro 1596837868705199",
                                          "to": "Счет 64686473678894779589"
                                          }) == 1

    # mock_get.assert_called_once_with(f"https://api.apilayer.com/exchangerates_data/convert", headers={'apikey': 'ws2JCB2959nUCODmE0dTTmn1joOQV2yf'}, params={'amount': '1', 'from': 'USD', 'to': 'RUB'})