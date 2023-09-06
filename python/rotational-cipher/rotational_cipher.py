"""Exercism Python3: Rotational Cipher

Problem: 
- Create a cipher that transposes letters in the alphabet based on a certain key.
- a ROT13 is a shift in the alphabet 13 to the right
"""

alpha_str = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    """Return a transposed string based on key"""

    transposed = ""
    for char in text:
        index = alpha_str.find(char.lower())

        # If char is not in alphabet
        if index == -1:
            transposed += char

        # Char is in alphabet
        else:
            shifted_index = index + key

            # account for over 25 limit
            if shifted_index > 25:
                shifted_index = shifted_index % 25 - 1

            # turn shifted index into char
            shifted_char = alpha_str[shifted_index]

            # account for capital
            if char.isupper():
                shifted_char = shifted_char.upper()

            transposed += shifted_char

    return transposed
