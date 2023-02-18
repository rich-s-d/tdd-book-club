import pytest
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


    def plus(self, addend):
        return Sum(Money(self.amount, self.currency_variable), addend)

    

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

    # I've not used an Expression Interface, so I've left the type checking for now.
    # See https://realpython.com/python-interface/ for details on python interfaces.
    def reduce(self, source, to: str):
        if type(source) == Money:
            return source
        else:
            sum: Sum = source
            return sum.reduce(to)


class Sum():
    def __init__(self, augend: Money, addend: Money):
        self.augend: Money = augend
        self.addend: Money = addend

    def reduce(self, to: str):
        amount: int = self.augend.amount + self.addend.amount
        return Money(amount, to)








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
