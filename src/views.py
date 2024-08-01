# from pathlib import Path
# import requests
# import logging
# import os
# from src.utils import processing_transaction
# from dotenv import load_dotenv
# #
# ROOTPATH = Path(__file__).resolve().parent.parent
# load_dotenv()
# Api_1 = os.getenv("API_KEY_CURRENCY")
# Api_2 = os.getenv("api_key_2")
#
# logging.basicConfig(
#     filename='app.log',
#     filemode='w', level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

#
# def card_information(list_tr):
#     """Функция для вывода информации по картам"""
#     try:
#         cards = []
#         unique_cards = set([transaction['Номер карты'] for transaction in list_tr])
#         for card_number in unique_cards:
#             total_expenses = 0
#             for transaction in list_tr:
#                 if transaction['Номер карты'] == card_number:
#                     total_expenses += transaction['Сумма операции']
#             cashback = abs(total_expenses // 100)
#             total = abs(total_expenses)
#             card_info = {
#                 "last_digits": card_number,
#                 "total_spent": total,
#                 "cashback": cashback
#             }
#             cards.append(card_info)
#         logging.info("Card information has been successfully received")
#         return {"cards": cards}
#     except Exception as e:
#         logging.error(f"Ошибка при получении информации по картам: {e}")
#         return {"cards": []}


#
# result = card_information()
# print(result)


# def top_transaction(my_list):
#     """Функция для вывода топ-5 транзакций по сумме платежа"""
#     try:
#         top_transactions = sorted(my_list, key=lambda x: x['Сумма платежа'], reverse=True)[:5]
#         result = {"top_transactions": []}
#         for transaction in top_transactions:
#             top_transaction = {
#                 "date": transaction['Дата операции'],
#                 "amount": transaction['Сумма платежа'],
#                 "category": transaction['Категория'],
#                 "description": transaction['Описание']
#             }
#             result["top_transactions"].append(top_transaction)
#         logging.info("The top 5 transactions were successfully received")
#         return result
#     except Exception as e:
#         logging.error(f"Ошибка при получении топ-5 транзакций: {e}")
#         return {"top_transactions": []}


# def get_currency_rates(api_key):
#     symbols = "EUR,USD,GBP,RUB"
#     url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}"
#     headers = {"apikey": api_key}
#
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Raises an HTTPError for bad response status
#
#         result = response.json()
#         currency_rates = []
#         for currency, rate in result["rates"].items():
#             currency_rates.append({
#                 "currency": currency,
#                 "rate": rate
#             })
#
#         return currency_rates
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error during request: {e}")
#         return []  # Return empty list on error
#
#
# def fetch_stock_prices(symbols, api_key):
#     """
#     Получает текущие цены акций для заданных символов.
#     """
#     stock_prices = []
#
#     for symbol in symbols:
#         url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
#
#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Поднимает исключение для 4xx и 5xx ошибок
#
#             result = response.json()
#             stock_data = result.get("Global Quote", {})
#             stock_symbol = stock_data.get("01. symbol")
#             stock_price = stock_data.get("05. price")
#
#             if stock_symbol and stock_price:
#                 stock_prices.append({"stock": stock_symbol, "price": float(stock_price)})
#                 logging.info(f"Цена акции {stock_symbol} успешно получена.")
#             else:
#                 logging.warning(f"Невозможно получить данные для {symbol}. Результат: {result}")
#
#         except requests.exceptions.HTTPError as http_err:
#             print(f"HTTP error occurred: {http_err}")
#             return []
#         except Exception as err:
#             print(f"Произошла ошибка: {err}")
#             return []
#
#     return stock_prices
from src.services import normalize_transactions, search_transactions
from src.utils import current_time, greeting, processing_transaction, card_information
from dotenv import load_dotenv
import os

load_dotenv()
Api_1 = os.getenv("API_KEY_CURRENCY")
Api_2 = os.getenv("api_key_2")


formater = current_time()

greeting_sms = greeting()
# list_transactions = processing_transaction()
# normal = normalize_transactions(list_transactions)

result = card_information(list_transactions)

top = top_transaction(list_transactions)

symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
Api_2 = "ваш_ключ_здесь"
stock_prices = fetch_stock_prices(symbols, Api_2)

api_key = Api_1
rates = get_currency_rates(api_key)

user_date = "31.12.2021"
category_word = "Супермаркеты"

filtered = get_expenses_by_category(normal, category_word, user_date)
total_expenses = sum(tx["Сумма операции"] for tx in filtered)

query = input("Введите слово для поиска: ")
search_result = search_transactions(normal, query)
