import pytest

from fizzbuzz import fizzBuzz


def test_returns1With1PassedIn():
    val = fizzBuzz(1)
    assert val == "1"

def test_resturns2With2PassedIn():
    val = fizzBuzz(2)
    assert val == "2"
