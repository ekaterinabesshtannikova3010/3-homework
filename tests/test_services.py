from src.services import search_transactions, normalize_transactions
import pytest


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


if __name__ == "__main__":
    test_search_description()
    test_search_category()
    test_search_no_results()
    print("All tests passed.")


def test_normalize_transactions():
    input_transactions = [
        {"Описание": "Покупка в магазине", "Категория": "Продукты", "Сумма": 100},
        {"Описание": 123, "Категория": "Развлечения", "Сумма": 200},
        {"Описание": "Поход в кино", "Категория": None, "Сумма": 300},
        {"Описание": None, "Категория": 456, "Сумма": 400},
    ]

    expected_output = [
        {"Описание": "Покупка в магазине", "Категория": "Продукты", "Сумма": 100},
        {"Описание": "123", "Категория": "Развлечения", "Сумма": 200},
        {"Описание": "Поход в кино", "Категория": "None", "Сумма": 300},
        {"Описание": "None", "Категория": "456", "Сумма": 400},
    ]

    assert normalize_transactions(input_transactions) == expected_output


if __name__ == "__main__":
    pytest.main()
