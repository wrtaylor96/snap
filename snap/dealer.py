from snap.deck import Deck
from snap.player import Player


class Dealer:
    def __call__(self, number_of_players: int, deck: Deck) -> list[Player]:
        deck.shuffle()
        deal_size = len(deck) // number_of_players
        return [
            Player(
                player_number=player_number + 1,
                # Deck is divided equally so not all cards may be dealt depending on number of players
                dealt_pile=deck[
                    player_number : number_of_players * deal_size : number_of_players
                ],
            )
            for player_number in range(number_of_players)
        ]
