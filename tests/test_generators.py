import pytest

from src.generators import transaction_descriptions


def test_transaction_descriptions():
    """
    Тестируем функцию-генератор для описания операций.
    """
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]

    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    assert descriptions == expected


@pytest.fixture
def card_number_generator_fixture():
    def format_card_number(card_number):
        return f"{card_number:016d}"

    def card_number_generator(start, end):
        for card_number in range(start, end + 1):
            yield format_card_number(card_number)

    return card_number_generator


def test_card_number_generator(card_number_generator_fixture):
    """
    Тестируем функцию-генератор номеров банковских карт.
    """
    card_gen = card_number_generator_fixture(1, 3)
    generated_numbers = list(card_gen)
    assert len(generated_numbers) == 3
    assert generated_numbers[0] == "0000000000000001"
    assert generated_numbers[1] == "0000000000000002"
    assert generated_numbers[2] == "0000000000000003"
