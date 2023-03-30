#!/usr/bin/python3

import os
os.environ["PYTHON_USELESS_UTILS_TIMER"] = "FALSE"

from comprehensions import simple_comprehension, simple_loop

def test_simple():
    inpt = ["a", "g", "c", "m", "d", "z"]
    expected_output = ["mm", "zz"]

    otpt_cmp = simple_comprehension(inpt)
    otpt_lp = simple_loop(inpt)

    assert otpt_cmp == otpt_lp
    assert expected_output == otpt_cmp

