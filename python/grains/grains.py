"""Exercism Python: Grains

Problem:
- there are 64 squares on a chess board
- for each subsequence square, the number of grain doubles starting with one
- we need to figure out that number of grain on the chessboard
"""

CHESS_BOARD_SQUARES = 64


def square(number: int) -> int:
    """Given a number of a square, get the number of grain on that square"""

    # if the number is not in range, raise error
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total() -> int:
    """Get the total amount of grain on the chessboard"""

    amount_of_grain = 0
    for i in range(CHESS_BOARD_SQUARES):
        amount_of_grain += square(i + 1)  # +1 because i starts at 0

    return amount_of_grain
