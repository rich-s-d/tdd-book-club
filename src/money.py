import pytest
#from dollar import Dollar
#from franc import Franc
from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount:int, currency: str) -> None:
        self.amount = amount
        self.currency_variable = currency

    def equals(self, object: object):
        money: Money = object
        print(self.__class__.__name__)
        #pytest.set_trace()
        return self.amount == money.amount and self.__class__.__name__ == money.__class__.__name__

    
    def dollar(amount: int):
        return Dollar(amount, "USD")

    def franc(amount: int):
        return Franc(amount, "CHF")

    @abstractmethod
    def times(self, multiplier: int):
        pass

    def currency(self):
        return self.currency_variable


class Franc(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)

    def times(self, multiplier) -> Money:
        return Money.franc(self.amount * multiplier)


class Dollar(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)
        
    def times(self, multiplier) -> Money:
        return Money.dollar(self.amount * multiplier)
