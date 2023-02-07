import random
from snap.dealer import Dealer
from snap.setting import DECK, MAX_PLAYERS, MIN_PLAYERS


def main():
    print("================== SETUP ==================")
    while True:
        try:
            number_of_players = int(input(f"Please enter the number of players between {MIN_PLAYERS} and {MAX_PLAYERS}: "))
        except ValueError:
            print(f"Please enter a valid number between {MIN_PLAYERS} and {MAX_PLAYERS}")
            continue

        if number_of_players < MIN_PLAYERS or number_of_players > MAX_PLAYERS:
            print(f"Please enter a valid number between {MIN_PLAYERS} and {MAX_PLAYERS}")
            continue
        else:
            break

    play_pile = []
    deck = DECK
    dealer = Dealer()
    players = dealer(
        number_of_players=number_of_players,
        deck=deck,
    )

    print("\n================== PLAY ===================")
    round: int = 0
    while [player for player in players if player.can_play]:
        round += 1
        print(f"\nRound {round}")
        for player in players:
            card = player.play_card()
            if card:
                play_pile.append(card)
            if len(play_pile) >= 2 and play_pile[-1] == play_pile[-2]:
                winning_player = random.choice(players)
                print(f"{winning_player.player_name}: \"SNAP!\"")
                winning_player.win_cards(play_pile)
                play_pile.clear()
        if play_pile:
            print(f"{len(play_pile)} cards discarded")
            play_pile.clear()
        print("Round finished")
    print("\nAll players are out of cards...")

    print("\n================== RESULTS ================")
    results = {
        player: len(player.win_pile)
        for player
        in players
    }
    for player, score in results.items():
        print(f"{player.player_name}: \"I scored {score} points\"")
    winner_names = [
        player.player_name
        for player, score
        in results.items()
        if score == max(results.values())
    ]
    print(f"The winner{' is' if len(winner_names) == 1 else 's are'} {' and '.join(winner_names)}. Congratulations!")
    print("GAME OVER")


if __name__ == '__main__':
    main()