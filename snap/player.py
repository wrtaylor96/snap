from snap.card import Card


class Player:
    player_name: str
    dealt_pile: list[Card]
    win_pile: list[Card]

    def __init__(self, player_number: int, dealt_pile: list[Card]) -> None:
        self.dealt_pile = dealt_pile
        self.player_name = f"Player {player_number}"
        self.win_pile = []
        print(f"{self.player_name} dealt {len(self.dealt_pile)} cards:")

    @property
    def can_play(self) -> bool:
        return bool(self.dealt_pile)

    def play_card(self) -> Card | None:
        card = self.dealt_pile.pop() if self.dealt_pile else None
        if card:
            print(f"{self.player_name} plays card {card}")
        else:
            print(f"{self.player_name} has no more cards to play")
        return card

    def win_cards(self, cards: list[Card]) -> None:
        print(f"{self.player_name} won {len(cards)} cards")
        self.win_pile.extend(cards)
