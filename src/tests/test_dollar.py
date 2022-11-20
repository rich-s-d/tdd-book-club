

import pytest
import sys
import os
# Add path to src modules.
sys.path.append(os.path.join(sys.path[0][:-5]))
from dollar import Dollar


def test_multiplication():
    #arrange
    five = Dollar(5)
    #act
    product: Dollar = five.times(2)
    #assert
    assert 10 == product.amount
    #act
    product: Dollar = five.times(3)
    #assert
    assert 15 == product.amount