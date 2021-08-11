import unittest
from unittest.mock import MagicMock

from poker.player import Player
from poker.hand import Hand

class PlayerTest(unittest.TestCase):

    def test_stores_name_and_hand(self):
        hand = Hand(cards = [])
        player = Player(name = "Hasan", hand = hand)
        self.assertEqual(player.name, "Hasan")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Hasan", hand = mock_hand)

        player.best_hand()
        mock_hand.best_rank.assert_called()