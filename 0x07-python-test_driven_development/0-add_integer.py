#!/usr/bin/python3

"""Creating a functions that sums two integers."""


def add_integer(a, b=98):
    """Defining the function functionalities."""
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        else:
            a = int(a)
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        else:
            b = int(b)
    return (a + b)
