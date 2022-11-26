

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

    #assert
    assert Dollar(10).equals(five.times(2))
    #act

    #assert
    assert Dollar(15).equals(five.times(3))


def test_equality():
    assert (Dollar(5).equals(Dollar(5)))
    assert not Dollar(5).equals(Dollar(6))
