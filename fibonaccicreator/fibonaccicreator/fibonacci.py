"""Compute values in the Fibonacci sequence using different approaches."""

from typing import Tuple

from memory_profiler import profile


@profile
def fibonacci_tuple(number: int) -> Tuple[int]:
    """Compute up to and including the number-th Fibonacci number using a tuple."""
    # create an empty tuple that will ultimately contain the results
    result = ()
    # set the initial conditions of the sequence
    a = 1
    b = 1
    # iterate from zero to the (number-1)th number
    for i in range(number):
        # store the value of a in the tuple
        result += (a,)
        # move to the next value such that:
        # a gets the current value of b
        # b gets the current value of a + b
        a, b = b, a + b
    # return the final tuple that contains the fibonacci numbers
    return result


@profile
def fibonacci_list(number: int) -> Tuple[int]:
    """Compute up to and including the number-th Fibonacci number using a list."""
    # create an empty list that will ultimately contain the results
    result = []
    # set the initial conditions of the sequence
    a = 1
    b = 1
    # iterate from zero to the (number-1)th number
    for i in range(number):
        # store the value of a in the list
        result.append(a)
        # move to the next value such that:
        # a gets the current value of b
        # b gets the current value of a + b
        a, b = b, a + b
    # return the final tuple that contains the fibonacci numbers
    return result
