import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):

    def test_validates_that_cards_have_three_of_the_same_rank(self):
        cards = [
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = ThreeOfAKindValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_return_three_of_a_kind_cards_from_card_collection(self):
        king_of_clubs = Card(rank = "King", suit = "Clubs")
        king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        king_of_spades = Card(rank = "King", suit = "Spades")
        
        cards = [
            Card(rank = "9", suit = "Clubs"),
            king_of_clubs,
            king_of_diamonds,
            king_of_spades,
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = ThreeOfAKindValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                king_of_clubs,
                king_of_diamonds,
                king_of_spades
            ]
        )