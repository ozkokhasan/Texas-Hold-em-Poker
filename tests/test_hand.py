import unittest
from poker.hand import Hand
from poker.card import Card

class HandTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "6", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.cards,
            cards
        )
    
    def test_figures_out_high_card_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )
    
    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "King", suit = "Diamonds")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )
    def test_figures_out_three_of_kind_is_best_rank(self):
        cards = [
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "King", suit = "Diamonds")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )