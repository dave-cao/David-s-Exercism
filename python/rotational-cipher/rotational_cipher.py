"""Exercism Python3: Rotational Cipher

Problem:
- Create the Caesar Cipher
- Rotate the text "key" amount of times to the right in the alphabet
"""

ALPHA = [*"abcdefghijklmnopqrstuvwxyz"]


def rotate(text, key):
    # if we reach the end (z) then we go back to A

    # match text with alpha, then rotate
    message = ""
    for char in text:
        if char.lower() in ALPHA:
            index = ALPHA.index(char.lower())
            rotation = index + key

            if rotation > 25:
                rotation = (rotation % 25) - 1  # -1 because index starts at 0

            new_char = ALPHA[rotation]
            if char.isupper():  # check if capital
                new_char = new_char.upper()

            message += new_char
        else:
            message += char

    return message


print(rotate("The brown fox.", 5))
# sbk
