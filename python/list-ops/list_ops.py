""" Exercism Python: List Ops

Problem:
- create the following list operations.
"""


def append(list1: list, list2: list) -> list:
    """Given two lists, add all items in the second list to the end of the first list"""
    return list1 + list2


def concat(lists: list[list]) -> list:
    """Given a series of lists, combine all items in all lists into one flattened
    list.
    """

    flat = []
    for list_item in lists:
        flat = append(flat, list_item)

    return flat


def filter(function, list: list) -> list:
    """Given a predicate, and a list, return the list of all items for which
    predicate(item) is true."""

    return [item for item in list if function(item)]


def length(list: list) -> int:
    """Given a list, return the total number of items within it"""

    count = 0
    for _ in list:
        count += 1

    return count


def map(function, list: list) -> list:
    """Given a function and a list, return the list of the results of applying
    function(item) on all items
    """

    return [function(item) for item in list]


def foldl(function, list: list, initial: int) -> int:
    """Given a function, a list, and initial accumulator, fold (reduce)
    each item into the accumulator from the left: similar to reduce"""

    acc = initial
    for item in list:
        acc = function(acc, item)

    return acc


def foldr(function, list: list, initial: int) -> int:
    """Given a function, a list, and an initial accumulator, fold (reduce)
    each item into the accumulator from the right."""

    acc = initial
    for i in range(len(list) - 1, -1, -1):
        item = list[i]
        acc = function(acc, item)

    return acc


def reverse(list: list) -> list:
    """Given a list, return a list with all the original items, but in
    reversed order."""

    return [list[i] for i in range(len(list) - 1, -1, -1)]
