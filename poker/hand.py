from poker.validators import (
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
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
            ("Straight Flush", StraightFlushValidator(cards = self.cards).is_valid),
            ("Four of a Kind", FourOfAKindValidator(cards = self.cards).is_valid),
            ("Full House", FullHouseValidator(cards = self.cards).is_valid),
            ("Flush", FlushValidator(cards = self.cards).is_valid),
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
        return StraightFlushValidator(cards = self.cards).is_valid() and self.cards[-1].rank == "Ace"

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }  