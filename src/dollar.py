


class Dollar:
    def __init__(self, amount) -> None:
        self.amount = amount
        
    def times(self, multiplier):
        #self.amount = self.amount * multiplier
        return Dollar(self.amount * multiplier)


    def equals(self, object: object):
        dollar: Dollar = object
        return self.amount == dollar.amount
        

    