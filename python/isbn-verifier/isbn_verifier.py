"""Exercism Python: ISBN Verifier

Problem:
- Given a string, check if the provided string is a valid ISBN-10 number
"""


def is_valid(isbn: str) -> bool:
    """Given an isbn string, check if it is a valid ISBN-10 number."""

    digits = [digit for digit in isbn if digit != "-"]
    digit_length = len(digits)  # record length of digits without dashes

    if not isbn:  # case of empty isbn
        return False

    if digits[-1] == "X":  # makes sure x only works as a last digit check
        digits = digits[:-1] + ["10"]

    digits = [
        digit for digit in digits if digit.isdigit()
    ]  # make sure every item is digit

    if len(digits) != 10 or digit_length != 10:  # makes sure i is not out of range
        return False

    return not sum(int(digits[10 + i * -1]) * i for i in range(10, 0, -1)) % 11
