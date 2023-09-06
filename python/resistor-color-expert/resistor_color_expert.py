"""Exercism Python: Resistor Color Expert"""

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

BAND_TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

PREFIX = ["", "kilo", "mega", "giga"]


def resistor_label(colors: list[str]) -> str:
    # unpack / set up variables
    if len(colors) > 3:
        *values, multiplier, tolerance = colors
    else:
        values, multiplier, tolerance = colors, "black", None

    # add the bands and apply multiplier
    val = ""
    for value in values:
        val += str(BAND_COLOR.index(value))
    val = int(val) * 10 ** BAND_COLOR.index(multiplier)

    # add proper prefix
    i = 0
    while val > 1000:
        val /= 1000
        i += 1

    # add tolerance if applicable
    display_str = f"{val:n} {PREFIX[i]}ohms"
    if tolerance:
        display_str += f" ±{BAND_TOLERANCE.get(tolerance)}%"

    return display_str
