import pytest
from src.widget import mask_account_card


@pytest.fixture
def ask_account():
    """Тестирование функции маскирующей счет."""
    return "Счет 73654108430135874305"


def test_mask_account_card(ask_account):
    assert mask_account_card(ask_account) == "Счет **4305"


def test_mask_account_card_m():
    assert mask_account_card
