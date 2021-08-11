from poker.validators import StraightValidator, FlushValidator

class StraightFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"
    
    def is_valid(self):
        if StraightValidator(cards = self.cards).is_valid():
            straight_cards = StraightValidator(cards = self.cards).valid_cards()
            if FlushValidator(cards = straight_cards).is_valid():
                return True
        return False

    def valid_cards(self):
        return StraightValidator(cards = self.cards).valid_cards()
    