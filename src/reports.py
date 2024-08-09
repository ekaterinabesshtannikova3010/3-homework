import datetime
import logging

logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def get_expenses_by_category(list_normal, word, date=None):
    """
    Функция для вывода трат по категорииза три месяца от задаваемой даты.
    """
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%d.%m.%Y").date()

    start_date = date - datetime.timedelta(days=90)
    filtered_transactions = [tx for tx in list_normal if word in tx["Категория"] and
                             start_date <= datetime.datetime.strptime(tx["Дата платежа"],
                                                                      "%d.%m.%Y").date() <= date]
    logging.info("Withdrawal of transactions in three months")
    return filtered_transactions
