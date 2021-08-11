from poker.validators import StraightFlushValidator, StraightValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Royal Flush"
    
    def is_valid(self):
        if StraightFlushValidator(cards = self.cards).is_valid():
            card = StraightFlushValidator(cards = self.cards).valid_cards()
            if card[-1] == "Ace":
                return True
        return False

    def valid_cards(self):
        return StraightValidator(cards = self.cards).valid_cards()