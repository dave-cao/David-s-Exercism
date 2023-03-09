"""Exercism Python: Raindrops.

Problem:
    - convert a number into a string that contains raindrop sounds depending
        on what that number factors into.
    - a factor is a nubmer that evenly divides into another number (no remainder)
    - Rule:
        - factor of 3: return "Pling"
        - factor of 5: return "Plang"
        - factor of 7: return "Plong"
        - else: return the digits
"""

from typing import Union


def convert(number: int) -> Union[str, int]:
    """Converts a number into raindrop sounds based on what it factors into.

    Params:
        - number(int): the number we are using to convert to raindrop sound

    Returns:
        - raindrop_sound(str): the raindrop sound that is produced.
    """

    raindrop_sound = ""
    if not number % 3:
        raindrop_sound += "Pling"
    if not number % 5:
        raindrop_sound += "Plang"
    if not number % 7:
        raindrop_sound += "Plong"

    return raindrop_sound or str(number)
