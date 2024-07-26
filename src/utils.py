import pandas as pd
from pathlib import Path
import os
import datetime
from config import file_xlsx
import logging
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

