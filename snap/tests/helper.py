from enum import Enum

from snap.deck import Deck


class TEST_SUIT_ENUM(Enum):
    SUIT_1 = "SUIT_1"
    SUIT_2 = "SUIT_2"


class TEST_VALUE_ENUM(Enum):
    VALUE_1 = "VALUE_1"
    VALUE_2 = "VALUE_2"
    VALUE_3 = "VALUE_3"


TEST_DECK = Deck(TEST_VALUE_ENUM, TEST_SUIT_ENUM)
