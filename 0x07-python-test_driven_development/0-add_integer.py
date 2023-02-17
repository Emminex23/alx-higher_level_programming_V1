#!/usr/bin/python3
"""This module contains a function that adds up integers"""


def add_integer(a, b=98):
    """This function adds up 2 integers and returns their sum.
       If the args is a float it is first converted to an integer.

       Args:
            a (int): The first integer
            b (int): The second integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    b = int(b)
    return a + b
