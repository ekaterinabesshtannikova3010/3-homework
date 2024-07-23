import json
from pathlib import Path
from typing import Any
# import logging
from config import ROOTPATH
import pandas as pd

# logger = logging.getLogger("__name__")
# file_handler = logging.FileHandler("../logs/.log",mode='w')
# file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
# logger.setLevel(logging.INFO)
# # logger.error("сhecking for errors")



def read_json_file(file_path: Any) -> list[dict]:
    """
    Функция для проверки JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


file_path = Path(ROOTPATH, "../data/operations.json")
transactions = read_json_file(file_path)
# print(transactions)
csv_file = '../data/transactions.csv'

def process_transaction():

    df_csv = pd.read_csv(csv_file, delimiter=";")
    df_csv["operationAmount"] = df_csv.apply(lambda row:
                   {"amount": row["amount"],"currensy": {"name": row["currency_name"], "code": row["currency_code"]}},
                                             axis=1)

    new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
    df_csv = df_csv[new_col_order]
    list_dict = df_csv.to_dict(orient="records")
    return list_dict


# print(process_transaction())




excel_file = '../data/transactions_excel.xlsx'


def processing_transaction():
    df_excel = pd.read_excel(excel_file)
    df_excel["operationAmount"] = df_excel.apply(lambda row:
                    {"amount": row["amount"],"currensy": {"name": row["currency_name"], "code": row["currency_code"]}},
                                                 axis=1)

    new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]
    df_excel = df_excel[new_col_order]
    list_dict = df_excel.to_dict(orient="records")
    return list_dict

# print(processing_transaction())
