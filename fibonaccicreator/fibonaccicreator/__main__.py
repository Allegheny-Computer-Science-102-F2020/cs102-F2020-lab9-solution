"""Define the command-line interface for the fibonaccicreator program."""

import typer

import os
import psutil
import sys

from resource import getrusage, RUSAGE_SELF


from fibonaccicreator import fibonacci

FIBONACCI_FUNCTION_BASE = "fibonacci"
UNDERSCORE = "_"


def format_bytes(size):
    """Format an output value in bytes in a human-readable fashion."""
    # Reference:
    # https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778
    power = 2 ** 10
    n = 0
    power_labels = {0: "", 1: "kilo", 2: "mega", 3: "giga", 4: "tera"}
    while size > power:
        size /= power
        n += 1
    return str(size) + " " + power_labels[n] + "bytes"


def main(
    approach: str = typer.Option(...),
    number: int = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
):
    """Create the list of Fibonacci values with a specified approach."""
    # display the debugging output for the program's command-line arguments
    typer.echo("")
    typer.echo(f"The chosen type of approach is {approach}!")
    typer.echo("")
    typer.echo(f"The program will compute the {number}th Fibonacci number! 🔢")
    typer.echo("")
    # construct the full name of the function to call
    function = FIBONACCI_FUNCTION_BASE + UNDERSCORE + approach
    # construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    function_to_call = getattr(fibonacci, function)
    # call the constructed function and capture the result
    fibonacci_result = function_to_call(number)
    # display debugging information with the function's output
    if display:
        typer.echo(f"  This is the output from {function}:")
        typer.echo("")
        # display the output from the computation
        typer.echo("  " + str(fibonacci_result))
        typer.echo("")
    # display a final message and some extra spacing, asking a question
    # about the efficiency of the approach to computing the number sequence
    typer.echo(
        "So, was this an efficient approach for computing the Fibonacci sequence? 🤷"
    )
    typer.echo("")
    process = psutil.Process(os.getpid())
    # display the estimated overall memory use as reported by the operating system
    # Reference:
    # https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
    typer.echo("Estimated overall memory according to the operating system:")
    typer.echo("   " + format_bytes(process.memory_info().vms))
    typer.echo("")
    # display the estimated peak memory use as reported by the operating system
    # Reference:
    # https://pythonspeed.com/articles/estimating-memory-usage/
    typer.echo("Estimated peak memory according to the operating system:")
    typer.echo("   " + format_bytes(getrusage(RUSAGE_SELF).ru_maxrss * 1024))
    typer.echo()
    # display the size of the dictionary
    # Reference:
    # https://www.geeksforgeeks.org/how-to-find-size-of-an-object-in-python
    # https://www.quora.com/How-much-memory-taken-by-variables-in-python
    typer.echo(f"Estimated size of the dictionary: {sys.getsizeof(fibonacci.fibonacci_storage)} bytes")


if __name__ == "__main__":
    typer.run(main)
