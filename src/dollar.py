from money import Money


class Dollar(Money):
    def __init__(self, amount) -> None:
        self.amount = amount
        
    def times(self, multiplier):
        #self.amount = self.amount * multiplier
        return Dollar(self.amount * multiplier)

