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
        return self.amount == money.amount and self.currency_variable == money.currency_variable


    def plus(self, added):
        return Money((self.amount + added.amount), self.currency_variable)

    

    def dollar(amount: int):
        return Money(amount, "USD")


    def franc(amount: int):
        return Money(amount, "CHF")


   # @abstractmethod
    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency_variable)


    #@abstractmethod
    def currency(self):
        return self.currency_variable

class Bank():
    def __init__(self) -> None:
        return None

    def reduce(self, source, to: str):
        return Money.dollar(10)










# Redundant with new code structure (we gutted the subclasses Franc and Dollar.)
# class Franc(Money):
#     def __init__(self, amount: int, currency: str) -> None:
#         super().__init__(amount, currency)

#     # def times(self, multiplier) -> Money:
#     #     # return Money.franc(self.amount * multiplier)
#     #     return Franc(self.amount * multiplier, self.currency)


# class Dollar(Money):
#     def __init__(self, amount: int, currency: str) -> None:
#         super().__init__(amount, currency)
        
#     # def times(self, multiplier) -> Money:
#     #     # return Money.dollar(self.amount * multiplier)
#     #     return Dollar(self.amount * multiplier, self.currency)
