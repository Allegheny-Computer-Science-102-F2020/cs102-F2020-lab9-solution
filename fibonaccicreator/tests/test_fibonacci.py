"""Add test cases for the functions in the fibonacci module."""

import sympy


from fibonaccicreator import fibonacci


def test_zeroth_fibonacci_default_iterative():
    """Ensure that the request for the Fibonacci iterative function works."""
    number = 0
    result = fibonacci.fibonacci_iterative(number)
    assert result == 1


def test_oneth_fibonacci_default_next_iterative():
    """Ensure that the request for the Fibonacci iterative function works."""
    number = 1
    result = fibonacci.fibonacci_iterative(number)
    assert result == 1


def test_sixth_fibonacci_iterative():
    """Ensure that the request for the Fibonacci iterative function works."""
    number = 6
    result = fibonacci.fibonacci_iterative(number)
    assert result == 13


def test_zeroth_fibonacci_default_recursive():
    """Ensure that the request for the Fibonacci recursive function works."""
    number = 0
    result = fibonacci.fibonacci_recursive(number)
    assert result == 1


def test_oneth_fibonacci_default_next_recursive():
    """Ensure that the request for the Fibonacci recursive function works."""
    number = 1
    result = fibonacci.fibonacci_recursive(number)
    assert result == 1


def test_sixth_fibonacci_recursive():
    """Ensure that the request for the Fibonacci recursive function works."""
    number = 6
    result = fibonacci.fibonacci_recursive(number)
    assert result == 13


def test_zeroth_fibonacci_default_recursive_memo():
    """Ensure that the request for the Fibonacci recursive function with memoization works."""
    number = 0
    result = fibonacci.fibonacci_memoized(number)
    assert result == 1


def test_oneth_fibonacci_default_next_recursive_memo():
    """Ensure that the request for the Fibonacci recursive function with memoization works."""
    number = 1
    result = fibonacci.fibonacci_memoized(number)
    assert result == 1


def test_sixth_fibonacci_recursive_memo():
    """Ensure that the request for the Fibonacci recursive with memoization function works."""
    number = 6
    result = fibonacci.fibonacci_memoized(number)
    assert result == 13
