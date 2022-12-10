import pytest
#from dollar import Dollar
#from franc import Franc
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount) -> None:
        self.amount = amount

    def equals(self, object: object):
        money: Money = object
        print(self.__class__.__name__)
        #pytest.set_trace()
        return self.amount == money.amount and self.__class__.__name__ == money.__class__.__name__

    
    def dollar(amount: int):
        return Dollar(amount)

    def franc(amount: int):
        return Franc(amount)

    # #@abstractmethod
    # def times(self, multiplier: int):
    #     return Money(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount) -> None:
        self.amount = amount
        
    def times(self, multiplier):
        #self.amount = self.amount * multiplier
        return Franc(self.amount * multiplier)
     


class Dollar(Money):
    def __init__(self, amount) -> None:
        self.amount = amount
        
    def times(self, multiplier):
        #self.amount = self.amount * multiplier
        return Dollar(self.amount * multiplier)