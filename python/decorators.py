#!/usr/bin/python3

# Anmol Kapoor

"""
In this file, you will find decorators used for testing the limits of particular functions
"""

import time
import os

TIMER = os.getenv("PYTHON_USELESS_UTILS_TIMER", "TRUE")


def timeit(func):
    """
    A simple decorator that times how long a function takes
    """
    def timer(*args, **kwargs):
        if TIMER != "TRUE":
            return func(*args, **kwargs)
        try:
            columns = os.get_terminal_size().columns
        except OSError as ose:  # error due to running in non-terminal environment (eg, IDLE)
            columns = 80  # assume default
        times = []
        for i in range(100000):
            start_time = time.time()
            result = func(*args, **kwargs)
            times.append(time.time() - start_time)
        average_time = sum(times) / len(times)
        print(f"{str(func.__name__).rjust((columns // 2) - 5)} : {average_time} seconds")
        return result
    return timer
