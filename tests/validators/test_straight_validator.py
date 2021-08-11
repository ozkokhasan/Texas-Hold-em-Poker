from poker.validators.straight_validator import StraightValidator
import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def test_determines_if_there_are_five_cards_in_row(self):
        two = Card(rank = "2", suit = "Spades")
        four = Card(rank = "4", suit = "Clubs")
        five = Card(rank = "5", suit = "Diamonds")
        six = Card(rank = "6", suit = "Spades")
        seven = Card(rank = "7", suit = "Diamonds")
        eight = Card(rank = "8", suit = "Clubs")
        nine = Card(rank = "9", suit = "Spades")
        cards = [
            two,
            four,
            five,
            six,
            seven,
            eight,
            nine
        ]

        validator = StraightValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_highest_cards_in_a_row(self):
        two = Card(rank = "2", suit = "Spades")
        four = Card(rank = "4", suit = "Clubs")
        five = Card(rank = "5", suit = "Diamonds")
        six = Card(rank = "6", suit = "Spades")
        seven = Card(rank = "7", suit = "Diamonds")
        eight = Card(rank = "8", suit = "Clubs")
        nine = Card(rank = "9", suit = "Spades")
        cards = [
            two,
            four,
            five,
            six,
            seven,
            eight,
            nine
        ]

        validator = StraightValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                five,
                six,
                seven,
                eight,
                nine
            ]
        )