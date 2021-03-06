"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence) -> bool:
    for i in range(len(data) - 2):
        if data[i] > data[i + 1]:    # to exclude non-sorted sequences
            return False
        if data[i] + data[i + 1] != data[i + 2]:    # to exclude non-fibonacci sequences     
            return False
    return True
