from src.services import normal
import datetime
import logging

logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

user_date = "31.12.2021"
category_word = "Супермаркеты"


def get_expenses_by_category(list_normal, word, date=None):
    """Функция для вывода трат по категорииза три месяца от задаваемой даты."""
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%d.%m.%Y").date()

    start_date = date - datetime.timedelta(days=90)
    filtered_transactions = [tx for tx in list_normal
    if word in tx["Категория"] and start_date <= datetime.datetime.strptime(tx["Дата платежа"],
                                                                            "%d.%m.%Y").date() <= date]
    logging.info("Withdrawal of transactions in three months")
    return filtered_transactions


filtered = get_expenses_by_category(normal, category_word, user_date)

total_expenses = sum(tx["Сумма операции"] for tx in filtered)
print(f"Траты на {"Супермаркеты"} за последние 3 месяца с {"31.12.2021"}: {total_expenses}")
