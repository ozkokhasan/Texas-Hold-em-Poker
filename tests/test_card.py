import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_card_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")
    
    def test_card_has_suit(self):
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_card_has_string_representation_with_rank_and_suit(self):
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")

    def test_card_has_technical_representation(self):
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")