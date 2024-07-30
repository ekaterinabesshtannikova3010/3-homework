from unittest.mock import patch
from src.services import search_transactions
import logging

# Пример функции search_transactions
def search_transactions(norm_transactions, query):
    """
    Функция для поиска транзакций по запросу.
    """
    filtered_transactions = [
        transaction for transaction in norm_transactions
        if query.lower() in transaction["Описание"].lower() or query.lower() in transaction["Категория"].lower()]
    logging.info(f"Search by query: '{query}'. Found {len(filtered_transactions)} transactions.")
    return filtered_transactions

def test_search_description():
    """
    Проверка поиска по описанию транзакции.
    """
    transactions = [
        {"Описание": "Покупка продуктов", "Категория": "Бытовые расходы"},
        {"Описание": "Оплата коммунальных услуг", "Категория": "Коммуналка"},
        {"Описание": "Поездка в отпуск", "Категория": "Путешествия"},
        {"Описание": "Оплата интернета", "Категория": "Связь"},
        {"Описание": "Ремонт квартиры", "Категория": "Строительство"},
    ]

    query = "покупка"
    result = search_transactions(transactions, query)
    assert len(result) == 1, "Expected 1 transaction to match the query."
    assert result[0]["Описание"] == "Покупка продуктов", "Expected the description to match."

def test_search_category():
    """
    Проверка поиска по категории транзакции.
    """
    transactions = [
        {"Описание": "Покупка продуктов", "Категория": "Бытовые расходы"},
        {"Описание": "Оплата коммунальных услуг", "Категория": "Коммуналка"},
        {"Описание": "Поездка в отпуск", "Категория": "Путешествия"},
        {"Описание": "Оплата интернета", "Категория": "Связь"},
        {"Описание": "Ремонт квартиры", "Категория": "Строительство"},
    ]

    query = "путешествия"
    result = search_transactions(transactions, query)
    assert len(result) == 1, "Expected 1 transaction to match the query."
    assert result[0]["Категория"] == "Путешествия", "Expected the category to match."

def test_search_no_results():
    """
    Проверка, что нет результатов при отсутствии совпадений.
    """
    transactions = [
        {"Описание": "Покупка продуктов", "Категория": "Бытовые расходы"},
        {"Описание": "Оплата коммунальных услуг", "Категория": "Коммуналка"},
        {"Описание": "Поездка в отпуск", "Категория": "Путешествия"},
        {"Описание": "Оплата интернета", "Категория": "Связь"},
        {"Описание": "Ремонт квартиры", "Категория": "Строительство"},
    ]

    query = "гаджет"
    result = search_transactions(transactions, query)
    assert len(result) == 0, "Expected no transactions to match the query."

# Запуск тестов
if __name__ == "__main__":
    test_search_description()
    test_search_category()
    test_search_no_results()
    print("All tests passed.")