from poker.validators import (
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator, 
    NoCardsValidator
)

class Hand():

    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)
    
    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy


    @property
    def _rank_validations_from_best_to_worst(self):
        return (
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind", self._four_of_a_kind),
            ("Full House", self._full_house),
            ("Flush", self._flush),
            ("Straight", StraightValidator(cards = self.cards).is_valid),
            ("Three of a Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
            ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
            ("Pair", PairValidator(cards = self.cards).is_valid),
            ("High Card", HighCardValidator(cards = self.cards).is_valid),
            ("No Cards", NoCardsValidator(cards = self.cards).is_valid)
        )
    def best_rank(self):
        for rank in self._rank_validations_from_best_to_worst:
            name, validator_method = rank
            if validator_method():
                return name

    def _royal_flush(self):
        return self._straight_flush() and self.cards[-1].rank == "Ace"

    def _straight_flush(self):
        return StraightValidator(cards = self.cards).is_valid() and self._flush()

    def _four_of_a_kind(self):
        ranks_with_three_of_kind = self._ranks_with_count(4)
        return len(ranks_with_three_of_kind) == 1

    def _full_house(self):
        return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()

    def _flush(self):
        suits_that_occurs_5_or_more_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }
        return len(suits_that_occurs_5_or_more_times) == 1

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts
    