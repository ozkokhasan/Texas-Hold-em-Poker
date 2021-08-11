import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_at_least_two_pairs(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Spades")
        ]

        validator = TwoPairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_collection_of_cards_that_have_pairs(self):
        king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        king_of_spades = Card(rank = "King", suit = "Spades")
        ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")
        ace_of_spades = Card(rank = "Ace", suit = "Spades")

        cards = [
            Card(rank = "9", suit = "Clubs"),
            king_of_diamonds,
            king_of_spades,
            ace_of_diamonds,
            ace_of_spades
        ]

        validator = TwoPairValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                king_of_diamonds,
                king_of_spades,
                ace_of_diamonds,
                ace_of_spades
            ]
        )