from snap.card import Card
from snap.player import Player
from snap.tests.helper import TEST_DECK


def test_can_play_true():
    assert Player(1, TEST_DECK.deck).can_play is True


def test_can_play_false():
    assert Player(1, []).can_play is False


def test_play_card_none_empty_hand():
    assert type(Player(1, TEST_DECK.deck).play_card()) == Card


def test_play_card_none_empty_hand():
    assert Player(1, []).play_card() is None


def test_win_cards():
    player = Player(1, [])
    assert player.win_pile == []
    player.win_cards(TEST_DECK.deck)
    assert player.win_pile == TEST_DECK.deck
