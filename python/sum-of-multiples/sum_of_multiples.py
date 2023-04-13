"""Exercism Python: Sum of Multiples.

Problem:
    - Given a number, find the sum of all the unique multiples of particular numbers
        up to but not including that number.
    - Eg: we're given [3, 5] with a limit of 20 -> first get all the multiples below 20
        of 3 and 5 and then add it all up.
"""


def sum_of_multiples(limit: int, multiples: list) -> int:
    """Given a list of multiples, find the sum of all the multiples of those numbers
    up to but not including a limit. The multiples are unique.

    Params:
        limit(int): the number we are going up to but not including
        multiples(list): a list of numbers that we want the multiples of.

    Returns:
        sum(factors)(int): the sum of all the multiples of those numbers up to but no
            including the limit.
    """
    return sum(
        {i for factor in multiples if factor for i in range(factor, limit, factor)}
    )
