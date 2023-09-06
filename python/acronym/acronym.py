"""Exercism Python: Acronym

Problem:
- convert a phrase to its acronym
- dashes ("-") are word separators like white space
- all other punctuation can be removed from input
"""


def abbreviate(words: str) -> str:
    """Turn a series of words into its acronym."""

    # filter words to replace "-" with space and get rid
    #   of all punctuation
    filter_words = ""
    for letter in words:
        # "-" is a valid seperator
        if letter == "-" or letter == " ":
            filter_words += " "

        # discard other punctuation
        if letter.isalpha():
            filter_words += letter

    # get the first letter of each word to create acronym
    acro = "".join(word[0].upper() for word in filter_words.split(" ") if word)

    return acro
