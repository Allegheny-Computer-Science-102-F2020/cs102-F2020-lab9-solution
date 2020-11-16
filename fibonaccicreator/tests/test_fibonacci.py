"""Add test cases for the functions in the fibonacci module."""

import sympy


from fibonaccicreator import fibonacci


def test_zeroth_fibonacci_default():
    """Ensure that the request for the Fibonacci iterative function works."""
    number = 0
    result = fibonacci.fibonacci_iterative(number)
    assert result == 1


def test_oneth_fibonacci_default_next():
    """Ensure that the request for the Fibonacci iterative function works."""
    number = 1
    result = fibonacci.fibonacci_iterative(number)
    assert result == 1


def test_sixth_fibonacci():
    """Ensure that the request for the Fibonacci iterative function works."""
    number = 6
    result = fibonacci.fibonacci_iterative(number)
    assert result == 13
