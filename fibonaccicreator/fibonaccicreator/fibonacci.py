"""Compute values in the Fibonacci sequence using different approaches."""

from memory_profiler import profile

# create an empty dictionary used for storage
# of previously computed Fibonacci values
fibonacci_storage = {}


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


@profile
def fibonacci_recursive(number: int) -> int:
    """Compute the number-th Fibonacci number using recursion."""
    # base case
    if number == 0 or number == 1:
        return 1
    # recursive case
    return fibonacci_recursive(number - 2) + fibonacci_recursive(number - 1)


@profile
def fibonacci_memoized(number: int) -> int:
    """Compute the number-th Fibonacci number using recursion."""
    # memoized case
    if number in fibonacci_storage:
        return fibonacci_storage[number]
    # base case
    elif number == 0 or number == 1:
        return 1
    # recursive case
    else:
        # perform the recursive computation
        result = fibonacci_recursive(number - 2) + fibonacci_recursive(number - 1)
        # store the value in the dictionary
        fibonacci_storage[number] = result
        # return the result
        return result
