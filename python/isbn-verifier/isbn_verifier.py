"""Exercism Python: ISBN Verifier

Problem:
- Given a string, check if the provided string is a valid ISBN-10 number
"""


def is_valid(isbn: str) -> bool:
    """Given an isbn string, check if it is a valid ISBN-10 number."""
    if not isbn:  # case of empty isbn
        return False

    digits = [digit for digit in isbn if digit != "-"]

    if digits[-1] == "X":
        digits[-1] = "10"

    # make sure isbn only has digits
    if len(digits) != 10 or not all(digit.isnumeric() for digit in digits):
        return False

    return not sum((int(digit) * (10 - i)) for i, digit in enumerate(digits)) % 11
