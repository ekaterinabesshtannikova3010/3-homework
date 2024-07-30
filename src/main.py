from src.utils import current_time, greeting, processing_transaction
from src.views import card_information, top_transaction, stock, currency
from src.reports import get_expenses_by_category
from src.services import normalize_transactions, search_transactions

formater = current_time()
print(formater)
greeting_sms = greeting()
print(f'"{greeting_sms}"')

list_transactions = processing_transaction()
normal = normalize_transactions(list_transactions)

result = card_information(list_transactions)
print(result)

top = top_transaction(list_transactions)
print(top)

print(stock)
print(currency)

user_date = "31.12.2021"
category_word = "Супермаркеты"

filtered = get_expenses_by_category(normal, category_word, user_date)
total_expenses = sum(tx["Сумма операции"] for tx in filtered)
print(f"Траты на {category_word} за последние 3 месяца с {user_date}: {abs(total_expenses)}")


query = input("Введите слово для поиска: ")
search_result = search_transactions(normal, query)
print(search_result)

