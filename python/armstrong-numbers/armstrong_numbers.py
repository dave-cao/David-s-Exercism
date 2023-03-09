"""Exercism Python: Armstrong Numbers

Problem:
    - An armstrong number is a number that is the sum of its own digits
        each raised to the power of the number of digits.
"""


def is_armstrong_number(number: int) -> bool:
    """Determine whether a number is an Armstrong number or not."""
    str_numbers = str(number)
    number_length = len(str_numbers)
    number_result = sum(int(str_number) ** number_length for str_number in str_numbers)

    return number_result == number
