def fizzBuzz(value):
    if isMultiple(value, 3):
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)


def isMultiple(value, mod):
    return (value % mod) == 0
