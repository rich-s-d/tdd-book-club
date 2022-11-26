


class Franc:
    def __init__(self, amount) -> None:
        self.amount = amount
        
    def times(self, multiplier):
        #self.amount = self.amount * multiplier
        return Franc(self.amount * multiplier)


    def equals(self, object: object):
        franc: Franc = object
        return self.amount == franc.amount
        

    