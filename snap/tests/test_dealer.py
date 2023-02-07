from snap.dealer import Dealer
from snap.tests.helper import TEST_DECK


def test_dealer_all_cards_dealt():
    dealer = Dealer()
    players = dealer(2, TEST_DECK)

    assert len(players) == 2
    for player in players:
        assert len(player.dealt_pile) == 3


def test_dealer_not_all_cards_dealt():
    dealer = Dealer()
    players = dealer(4, TEST_DECK)

    assert len(players) == 4
    for player in players:
        assert len(player.dealt_pile) == 1
