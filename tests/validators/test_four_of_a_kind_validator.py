import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.clubs = Card(rank = "3", suit = "Clubs")
        self.diamonds = Card(rank = "3", suit = "Diamonds")
        self.hearts = Card(rank = "3", suit = "Hearts")
        self.spades = Card(rank = "3", suit = "Spades")

        self.cards = [
            Card(rank = "2", suit = "Clubs"),
            self.clubs,
            self.diamonds,
            self.hearts,
            self.spades,
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "9", suit = "Spades")
        ]
    def test_determines_that_four_cards_of_one_rank_are_present(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_four_cards_with_same_rank(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.clubs,
                self.diamonds,
                self.hearts,
                self.spades
            ]
        )
    