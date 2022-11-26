


class Money:
    def __init__(self, amount) -> None:
        self.amount = amount

    def equals(self, object: object):
        money: Money = object
        return self.amount == money.amount