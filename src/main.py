from src.utils import formater, greeting_sms
from src.views import result, top, stock, currency
from src.reports import total_expenses
from src.services import search_result


print(formater)
print(f'"{greeting_sms}"')
print(result)
print(top)
print(stock)
print(currency)
print(f"Траты на {"Супермаркеты"} за последние 3 месяца с {"31.12.2021"}: {abs(total_expenses)}")
print(search_result)
