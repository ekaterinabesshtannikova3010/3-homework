import pandas as pd
from pathlib import Path
from config import file_xlsx
import datetime
import requests
import os
from dotenv import load_dotenv
import logging

ROOTPATH = Path(__file__).resolve().parent.parent

logging.basicConfig(
    filename='app.log',
    filemode='w', level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def processing_transaction():
    """Функция для обработки Еxcel файла."""
    try:
        df_excel = pd.read_excel(Path(ROOTPATH, file_xlsx), engine="openpyxl")
        list_dict = df_excel.to_dict(orient="records")
        logging.info("Successfully processed transactions from an Excel file")
        return list_dict
    except Exception as e:
        logging.error(f"Ошибка при обработке транзакций: {e}")
        return []


list_transactions = processing_transaction()


# print(list_transactions[1])

def current_time():
    """Функция для получения текущего времени."""
    try:
        xt = datetime.datetime.now()
        formate_time = xt.strftime("%H:%M:%S")
        logging.info(f"The current time is received: {formate_time}")
        return formate_time
    except Exception as e:
        logging.error(f"Ошибка при получении текущего времени: {e}")
        return "00:00:00"


formater = current_time()


# print(formater)

def greeting():
    """Функция для вывода приветствия в соответствии времени на данный момент"""
    try:
        xt = datetime.datetime.now()
        current_time = xt.hour
        if 5 <= current_time < 12:
            greeting_sms = "Доброе утро"
        elif 12 <= current_time < 18:
            greeting_sms = "Добрый день"
        elif 18 <= current_time < 23:
            greeting_sms = "Добрый вечер"
        else:
            greeting_sms = "Доброй ночи"
        logging.info(f"A greeting has been formed: {greeting_sms}")
        return greeting_sms
    except Exception as e:
        logging.error(f"Ошибка при формировании приветствия: {e}")
        return "Приветствие"


greeting_sms = greeting()
# print(f'"{greeting_sms}"')


def card_information():
    """Функция для вывода информации по картам"""
    try:
        cards = []
        unique_cards = set([transaction['Номер карты'] for transaction in list_transactions])
        for card_number in unique_cards:
            total_expenses = 0
            for transaction in list_transactions:
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


result = card_information()


# print(result)


def top_transaction(list_transactions):
    """Функция для вывода топ-5 транзакций по сумме платежа"""
    try:
        top_transactions = sorted(list_transactions, key=lambda x: x['Сумма платежа'], reverse=True)[:5]
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

top = top_transaction(list_transactions)
# print(top)


api = "U2JDIP01ZL7AS9PL"
symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
stock_prices = []

for symbol in symbols:
    """Вывод стоимости указанных акций(P.S.не больше 25 запросов в сутки,в останьнм случае выводит "200")"""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api}"

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

symbols = "EUR,USD,GBP,RUB"
url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}"

payload = {}
headers = {
    "apikey": "03mmVsXS6y4lRrzEKToy0AINpbtQxKob"
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