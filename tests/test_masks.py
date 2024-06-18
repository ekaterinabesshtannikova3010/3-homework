import pytest
from src.masks import get_mask_card_number


def test_get_mask_card_number(get_mask):
    assert get_mask_card_number(get_mask) == "7000 79** **** 6361"


def test_get_mask_card_number_m():
    assert get_mask_card_number


@pytest.mark.parametrize("mask, expected", [("7000792289606361", "7000 79** **** 6361"),
                                            ("7000792289608963", "7000 79** **** 8963")])
def test_get_mask_card(mask, expected):
    assert get_mask_card_number(mask) == expected
