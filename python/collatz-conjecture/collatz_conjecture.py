"""Exercism Python: Collatz Conjecture.

Problem
    - The 3x+1 problem
    - If n is even, divide n by 2 to get n / 2
    - If n is odd, multiply n by 3 and add 1 to get 3n + 1
    - The conjecture states that no matter what number you start with, you will
        always reach 1 eventually.
"""


def steps(number: float) -> int:
    """Output the number of steps it takes to reach 1 using the Collatz Conjecture."""

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number > 1:
        if number % 2:  # odd
            number = 3 * number + 1
        else:  # even
            number /= 2
        count += 1
    return count
