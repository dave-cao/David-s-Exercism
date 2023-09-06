"""Exercism Python: Binary Search

Problem:
- implement a binary search algorithm
"""


def find(search_list: list[int], value: int) -> int:
    """
    Given a sorted list of numbers, use binary search to get the index
    of where [value] is in the sorted list.
    """

    low = 0
    high = len(search_list) - 1

    while True:
        if low > high:
            raise ValueError("value not in array")

        # find the middle element
        middle_index = ((high - low) // 2) + low
        middle_number = search_list[middle_index]

        # compare middle element with target
        if middle_number == value:
            return middle_index

        elif middle_number < value:
            # discard all lower numbers
            low = middle_index + 1

        else:
            # discard all higher numbers
            high = middle_index - 1
