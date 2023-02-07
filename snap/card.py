from enum import Enum
from typing import Any


class Card:
    suit: Enum
    value: Enum

    def __init__(self, suit: Any, value: Any) -> None:
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{str(self.value.value)} of {str(self.suit.value)}"

    def __eq__(self, other: "Card"):
        return other.suit == self.suit or other.value == self.value


class Standard52SuitEnum(Enum):
    CLUBS = "CLUBS"
    DIAMONDS = "DIAMONDS"
    HEARTS = "HEARTS"
    SPADES = "SPADES"


class Standard52ValueEnum(Enum):
    ACE = "ACE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"
    SIX = "SIX"
    SEVEN = "SEVEN"
    EIGHT = "EIGHT"
    NINE = "NINE"
    TEN = "TEN"
    JACK = "JACK"
    QUEEN = "QUEEN"
    KING = "KING"
