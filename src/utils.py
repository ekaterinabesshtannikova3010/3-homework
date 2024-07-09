import json
from pathlib import Path
from typing import Any
import logging
from src.config import ROOTPATH

logger = logging.getLogger("__name__")
file_handler = logging.FileHandler("../logs/.log")
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)
logger.error("сhecking for errors")


def read_json_file(file_path: Any) -> list[dict]:
    """
    Функция для проверки JSON-файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                logging.info(f"Успешно прочитан файл: {file_path}")
                return data
            except json.JSONDecodeError:
                logging.error("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logging.error(f"Файл не найден: {file_path}")
        return []


file_path = Path(ROOTPATH, "../data/operations.json")
transactions = read_json_file(file_path)
print(transactions)
