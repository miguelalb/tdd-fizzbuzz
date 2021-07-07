import pytest

from fizzbuzz import fizzBuzz

def test_canCallFizzBuzz():
    fizzBuzz(1)

def test_returns1With1PassedIn():
    val = fizzBuzz(1)
    assert val == "1"
