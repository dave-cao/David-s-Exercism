"""Exercism Python: Square Root """


def square_root(number: int) -> int:
    """Given a natural radicand, return its square root."""

    # find all the squares less than number
    # if you find a match, then return the square root
    i = 1
    while i * i < number:
        i += 1

    return i
