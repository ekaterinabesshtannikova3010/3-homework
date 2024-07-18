import re
from typing import Any
from src.utils import transactions


def description_transactions(transactions: Any, description) -> list[dict]:
    """Реализуем функцию скорорая выводит список словарей в котором есть значение."""
    results = []
    pattern = re.compile(description, re.IGNORECASE)

    for transaction in transactions:
        for key, value in transaction.items():
            if isinstance(value, str) and re.search(pattern, value):
                results.append(transaction)
                break

    return results


description = "Перевод организации"
filtered_transactions = description_transactions(transactions, description)


# print(filtered_transactions)

def count_operations_by_category(transactions, categories):
    category_count = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count


categories = ["Перевод организации", "Перевод со счета на счет", "Открытие вклада", "Перевод с карты на счет"]
category_count = count_operations_by_category(transactions, categories)

# print(category_count)