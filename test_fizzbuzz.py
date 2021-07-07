import pytest

from fizzbuzz import fizzBuzz


def checkFizzBuzz(value, expected):
    val = fizzBuzz(value)
    assert val == expected


def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")
