import pytest

from fizzbuzz import fizzBuzz


def checkFizzBuzz(value, expected):
    val = fizzBuzz(value)
    assert val == expected


def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_resturns2With2PassedIn():
    checkFizzBuzz(2, "2")
