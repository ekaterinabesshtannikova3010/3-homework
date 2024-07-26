from src.utils import list_transactions
import logging

logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def normalize_transactions(list_transactions):
    """
    Функция для приведения значений по ключам "Описание" и "Категории"
    к единому типу данных.
    """
    transactions = []
    for transaction in list_transactions:
        description = str(transaction.get("Описание", ""))
        category = str(transaction.get("Категория", ""))
        trans = {
            "Описание": description,
            "Категория": category,
            **{k: v for k, v in transaction.items() if k not in ["Описание", "Категория"]}
        }
        transactions.append(trans)
        # logging.info("The values for the key to a single data type are given")
    return transactions


normal = normalize_transactions(list_transactions)


# print(normal)


def search_transactions(norm_transactions):
    """
    Функция для поиска транзакций по запросу.
    """
    # query = input("Введите слово для поиска: ")
    query = "Красота"
    filtered_transactions = [
        transaction for transaction in norm_transactions
        if query.lower() in transaction["Описание"].lower() or query.lower() in transaction["Категория"].lower()]
    logging.info(f"Search by query: '{query}'. Found {len(filtered_transactions)} transactions.")
    return filtered_transactions


# Пример использования
search_result = search_transactions(normal)
# print(search_result)
