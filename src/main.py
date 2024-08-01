from src.views import formater, greeting_sms, card_information, top, total_expenses, search_result
from src.utils import processing_transaction
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# Api_1 = os.getenv("API_KEY_CURRENCY")
# Api_2 = os.getenv("api_key_2")
#
#
# formater = current_time()
# print(formater)
# greeting_sms = greeting()
# print(f'"{greeting_sms}"')
#
# list_transactions = processing_transaction()
# normal = normalize_transactions(list_transactions)
#
# result = card_information(list_transactions)
# print(result)
#
# top = top_transaction(list_transactions)
# print(top)
#
# #
# # symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
# # Api_2 = "ваш_ключ_здесь"
# # stock_prices = fetch_stock_prices(symbols, Api_2)
# # print(stock_prices)
#
# # api_key = Api_1
# # rates = get_currency_rates(api_key)
# # print(rates)
#
# user_date = "31.12.2021"
# category_word = "Супермаркеты"
#
# filtered = get_expenses_by_category(normal, category_word, user_date)
# total_expenses = sum(tx["Сумма операции"] for tx in filtered)
# print(f"Траты на {category_word} за последние 3 месяца с {user_date}: {abs(total_expenses)}")
#
#
# query = input("Введите слово для поиска: ")
# search_result = search_transactions(normal, query)
# print(search_result)
print(formater)
print(greeting_sms)
list_transactions = processing_transaction()
normal = normalize_transactions(list_transactions)
print(result)
print(top)
user_date = "31.12.2021"
category_word = "Супермаркеты"
print(f"Траты на {category_word} за последние 3 месяца с {user_date}: {abs(total_expenses)}")
print(search_result)