from src.utils import (processing_transaction, top_transaction, current_time, greeting, card_information,
                       fetch_stock_prices, get_currency_rates, Api_1)
from src.services import normalize_transactions, search_transactions
from src.reports import get_expenses_by_category
import json
from dotenv import load_dotenv
from pathlib import Path

ROOTPATH = Path(__file__).resolve().parent.parent
load_dotenv()

with open("../user_settings.json") as file:
    symbols = json.load(file)["user_stocks"]

formater = current_time()
greeting_sms = greeting()
print(formater)
print(greeting_sms)

list_transactions = processing_transaction()
result = card_information(list_transactions)
top = top_transaction(list_transactions)

normal = normalize_transactions(list_transactions)

user_date = "31.12.2021"
category_word = "Супермаркеты"

filtered = get_expenses_by_category(normal, category_word, user_date)
total_expenses = sum(tx["Сумма операции"] for tx in filtered)

query = input("Введите слово для поиска: ")
search_result = search_transactions(normal, query)

print(result)
print(top)

print(f"Траты на {category_word} за последние 3 месяца с {user_date}: {abs(total_expenses)}")
print(search_result)


stock_prices = fetch_stock_prices(symbols)
rates = get_currency_rates()

print(stock_prices)
print(rates)
