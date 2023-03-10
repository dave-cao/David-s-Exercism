"""Exercism Python: Flatten Array

Problem:
- Take a nested list and return a single flattened list with all values except nill
    and null.
"""


flattend_list = []


def flatten(iterable: list) -> list:
    """Flattens a nested list and outputs a single list leaving out null values."""

    if type(iterable) != list:  # base case
        if iterable is not None:
            flattend_list.append(iterable)
        return []

    for item in iterable:  # continue digging deeper into list until unnested
        flatten(item)

    return flattend_list
