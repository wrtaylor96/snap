import random
from enum import Enum
from snap.card import Card, Standard52SuitEnum, Standard52ValueEnum


class Deck:
    deck: list[Card]
    _current_index: int

    def __init__(self, value_enum: Enum, suit_enum: Enum) -> None:
        self.deck = [
            Card(
                suit=suit,
                value=value,
            )
            for value in value_enum
            for suit in suit_enum
        ]
        self._current_index = 0

    def __str__(self):
        return "\n".join([str(card) for card in self.deck])

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self):
            card = self.deck[self._current_index]
            self._current_index += 1
            return card

        raise StopIteration

    def __getitem__(self, idx):
        return self.deck[idx]

    def shuffle(self) -> None:
        random.shuffle(self.deck)
        print("Deck shuffled")


class Standard52Deck(Deck):
    def __init__(self) -> None:
        super(Standard52Deck, self).__init__(Standard52ValueEnum, Standard52SuitEnum)
