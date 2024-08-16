import pandas as pd
from pathlib import Path
import datetime
from config import file_xlsx
import requests
import logging
import os
from dotenv import load_dotenv
import json

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


def current_time():
    """
    Функция для получения текущего времени."""
    try:
        xt = datetime.datetime.now()
        formate_time = xt.strftime("%H:%M:%S")
        logging.info(f"The current time is received: {formate_time}")
        return formate_time
    except Exception as e:
        logging.error(f"Ошибка при получении текущего времени: {e}")
        return "00:00:00"


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


def get_currency_rates():
    with open("../user_settings.json") as file:
        symbols = ",".join(json.load(file)["user_currencies"])
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}"
    headers = {"apikey": Api_1}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        currency_rates = []
        for currency, rate in result["rates"].items():
            currency_rates.append({
                "currency": currency,
                "rate": rate
            })

        return currency_rates

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return []


def fetch_stock_prices(symbols):
    """
    Получает текущие цены акций для заданных символов.
    """
    stock_prices = []

    for symbol in symbols:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={Api_2}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            result = response.json()
            stock_data = result.get("Global Quote", {})
            stock_symbol = stock_data.get("01. symbol")
            stock_price = stock_data.get("05. price")

            if stock_symbol and stock_price:
                stock_prices.append({"stock": stock_symbol, "price": float(stock_price)})
                logging.info(f"Цена акции {stock_symbol} успешно получена.")
            else:
                logging.warning(f"Невозможно получить данные для {symbol}. Результат: {result}")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return []
        except Exception as err:
            print(f"Произошла ошибка: {err}")
            return []

    return stock_prices
