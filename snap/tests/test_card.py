from snap.card import Card
from snap.tests.helper import TEST_SUIT_ENUM, TEST_VALUE_ENUM


def test_card_equal():
    assert Card(TEST_SUIT_ENUM.SUIT_1, TEST_VALUE_ENUM.VALUE_1) == Card(
        TEST_SUIT_ENUM.SUIT_1, TEST_VALUE_ENUM.VALUE_1
    )
    assert Card(TEST_SUIT_ENUM.SUIT_1, TEST_VALUE_ENUM.VALUE_1) == Card(
        TEST_SUIT_ENUM.SUIT_1, TEST_VALUE_ENUM.VALUE_2
    )
    assert Card(TEST_SUIT_ENUM.SUIT_1, TEST_VALUE_ENUM.VALUE_1) == Card(
        TEST_SUIT_ENUM.SUIT_2, TEST_VALUE_ENUM.VALUE_1
    )


def test_card_not_equal():
    assert Card(TEST_SUIT_ENUM.SUIT_1, TEST_VALUE_ENUM.VALUE_1) != Card(
        TEST_SUIT_ENUM.SUIT_2, TEST_VALUE_ENUM.VALUE_2
    )
