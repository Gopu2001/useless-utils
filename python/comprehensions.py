#!/usr/bin/python3

# Anmol Kapoor

"""
In this file, you will find examples of how to perform comprehensions of for loops, primarily
into lists and dictionaries, after taking in data of various types.
"""

from typing import List

from decorators import timeit


@timeit
def simple_loop(arr: List[str]) -> List[str]:
    """
    Perform a simple for loop and add a copy of the string to the end if the string's first
    character is between 'm' and 'z', inclusive on both ends. Otherwise, do not add the string
    """
    result = []

    for element in arr:
        if element[0].lower() in "mnopqrstuvwxyz":
            result.append(element * 2)

    return result


@timeit
def simple_comprehension(arr: List[str]) -> List[str]:
    """
    Perform a simple list comprehension and add a copy of the string to the end if the string's
    first character is between 'm' and 'z', inclusive on both ends. Otherwise, do not add the
    string
    """
    result = [element * 2 for element in arr if element[0].lower() in "mnopqrstuvwxyz"]

    return result


if __name__ == "__main__":
    simple_comprehension(list("abcghimnostuyz"))
    simple_loop(list("abcghimnostuyz"))
