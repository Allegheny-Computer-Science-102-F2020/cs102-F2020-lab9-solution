"""Compute values in the Fibonacci sequence using different approaches."""

from memory_profiler import profile


@profile
def fibonacci_iterative(number: int) -> int:
    """Compute the number-th Fibonacci number using iteration."""
    # set the initial conditions for the calculation
    a = 1
    b = 1
    # iterate from zero to the (number-1)th number
    for i in range(number):
        # move to the next value such that:
        # a gets the current value of b
        # b gets the current value of a + b
        a, b = b, a + b
    # return the final tuple that contains the fibonacci numbers
    return a
