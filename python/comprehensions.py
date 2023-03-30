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


@timeit
def double_loop(img: List[List[int]]) -> List[int]:
    """
    Perform a double for loop and flatten a 2D image
    """
    result = []

    for y in img:
        for x in y:
            result.append(x)

    return result


@timeit
def double_comprehension(img: List[List[int]]) -> List[int]:
    """
    Perform a double list comprehension and flatten a 2D image
    """
    result = [x for y in img for x in y]

    return result


if __name__ == "__main__":
    string_test = ["a", "b", "c", "g", "h", "i", "m", "n", "o", "s", "t", "u", "y", "z"]
    simple_comprehension(string_test)
    simple_loop(string_test)
    print()

    img_test = [
        [0,1,2,1],
        [2,3,4,3],
        [4,5,6,3],
        [1,0,5,2]
    ]
    double_comprehension(img_test)
    double_loop(img_test)
