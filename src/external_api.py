import requests
import os
from dotenv import load_dotenv
from pathlib import Path

from typing import Any
from src.utils import transactions

ROOT_PATH = Path(__file__).resolve().parent.parent
env_path = ROOT_PATH / '.env'
load_dotenv(env_path)

apikey = os.getenv("API_KEY")


def convert_transaction_to_rubles(transaction: Any) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает ее сумму в рублях.
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {'apikey': "aFrM6l6mBleUeAR41wRBEk2iBqB6hZ1c"}
    response = requests.request("GET", url, headers=headers)
    result = response.json()
    return result["result"]



print(convert_transaction_to_rubles(transactions[1]))
