from pathlib import Path
import requests
import logging
import os
from src.utils import processing_transaction
from dotenv import load_dotenv

ROOTPATH = Path(__file__).resolve().parent.parent
load_dotenv()
Api_1 = os.getenv("API_KEY_CURRENCY")
Api_2 = os.getenv("api_key_2")

logging.basicConfig(
    filename='app.log',
    filemode='w', level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def card_information(list_tr):
    """Функция для вывода информации по картам"""
    try:
        cards = []
        unique_cards = set([transaction['Номер карты'] for transaction in list_tr])
        for card_number in unique_cards:
            total_expenses = 0
            for transaction in list_tr:
                if transaction['Номер карты'] == card_number:
                    total_expenses += transaction['Сумма операции']
            cashback = abs(total_expenses // 100)
            total = abs(total_expenses)
            card_info = {
                "last_digits": card_number,
                "total_spent": total,
                "cashback": cashback
            }
            cards.append(card_info)
        logging.info("Card information has been successfully received")
        return {"cards": cards}
    except Exception as e:
        logging.error(f"Ошибка при получении информации по картам: {e}")
        return {"cards": []}

#
# result = card_information()


# print(result)


def top_transaction(my_list):
    """Функция для вывода топ-5 транзакций по сумме платежа"""
    try:
        top_transactions = sorted(my_list, key=lambda x: x['Сумма платежа'], reverse=True)[:5]
        result = {"top_transactions": []}
        for transaction in top_transactions:
            top_transaction = {
                "date": transaction['Дата операции'],
                "amount": transaction['Сумма платежа'],
                "category": transaction['Категория'],
                "description": transaction['Описание']
            }
            result["top_transactions"].append(top_transaction)
        logging.info("The top 5 transactions were successfully received")
        return result
    except Exception as e:
        logging.error(f"Ошибка при получении топ-5 транзакций: {e}")
        return {"top_transactions": []}


# top = top_transaction(list_transactions)
# print(top)


symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
stock_prices = []

for symbol in symbols:
    """Вывод стоимости указанных акций(P.S.не больше 25 запросов в сутки,в остальном случае выводит "200")"""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={Api_2}"

    response = requests.get(url)
    # print(response)

    if response.status_code == 200:
        result = response.json()
        stock_data = result.get("Global Quote", {})
        stock_symbol = stock_data.get("01. symbol")
        stock_price = stock_data.get("05. price")
        if stock_symbol and stock_price:
            stock_prices.append({"stock": stock_symbol, "price": float(stock_price)})
        logging.info("Share amounts have been successfully received")
    else:
        print(f"Error {response.status_code}: {response.json().get('Error Message', 'Unknown error')}")

stock = {"stock_prices": stock_prices}
# print(stock)

"""Получение значений курса валют."""
symbols = "EUR,USD,GBP,RUB"
url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}"

payload = {}
headers = {
    "apikey": Api_1
}
response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.json()

if status_code == 200:
    currency_rates = []
    for currency, rate in result["rates"].items():
        currency_rates.append({
            "currency": currency,
            "rate": rate
        })
        currency = {"currency_rates": currency_rates}
#     print(currency)
# else:
#     print(f"Error {status_code}: {result['error']['message']}")
