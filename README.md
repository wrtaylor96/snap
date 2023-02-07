## Snap Background
Snap! is a card game where all of the cards are shuffled and dealt equally to players (a group of 2, 3 or 4 people).
Each player in turn turns over the top card from their face down dealt pile and puts it on top of their face up pile.
When someone turns over a card that matches the value (same number, or same face) of a card on top of another player's face up pile, the players race to be the first to say “Snap!”
The player who says “Snap!” first wins both piles and adds them to their winning pile.
If more than one player says “Snap!” at the same time, the two piles are combined into the snap pot.
Whoever wins the next snap wins the whole pot.
At the end of the game, when all players have dealt their original hand of cards. The player with the most cards wins the game.

## Snap Requirements
1. The application should ask the user how many playing card decks to play with
2. The application should shuffle the decks before play commences
3. Games of snap should now be simulated. Cards are played one at a time and when two matching cards are dealt one after another the first player to shout snap wins. (You do not need to implement the case of a draw round)
4. The winner of each round collects all the cards dealt in this round
5. Once all cards in the deck are exhausted the application should declare the winner based on who has the most won cards

## Requirments
- Python 3.10

## Run a game of Snap
```python main.py```

## Run unit tests
```pip install pytest```

```pytest```
