"""Exercism Python: Resistor Color Trio

Problem:
- 
"""
BAND_COLOR = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def label(colors: list[str]) -> str:
    """Given a list of colours, determine the amount of ohms.

    For example:
        - ["orange", "orange", "black"] would output "33 ohms"
        - ["orange", "orange", "orange"] would output "33000 kiloohms"
    """

    # grabbed the value of each color of colors
    first_value, second_value, num_zeros, *_ = [
        BAND_COLOR.index(color) for color in colors
    ]

    # combine the first and second value
    value = int(str(first_value) + str(second_value))

    # add number of zeros to value
    value *= 10**num_zeros

    # convert value to its metric equivalent
    i = 0
    while value > 0 and value % 1000 == 0:
        value //= 1000
        i += 1
    prefix = ["", "kilo", "mega", "giga"]

    return f"{value} {prefix[i]}ohms"
