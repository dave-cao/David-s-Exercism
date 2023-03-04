"""Exercism Python: Leap"""


def leap_year(year: int) -> bool:
    """Given a year, determine if it is a leap year or not. Return True or False."""

    # it is divisible by 4
    # except if it is evenly divisible by 100
    # unless the year is also evenly divisible by 400

    if not year % 4:  # year is divisible by 4
        if not year % 100:  # year is divisible by 100
            return not year % 400  # return true if divisible by 400

        return True
    return False
