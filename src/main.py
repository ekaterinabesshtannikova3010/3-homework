from src.views import formater, greeting_sms, card_information, stock_prices, rates
from src.utils import processing_transaction, top_transaction
from src.services import normalize_transactions, search_transactions
from src.reports import get_expenses_by_category

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

print(stock_prices)
print(rates)