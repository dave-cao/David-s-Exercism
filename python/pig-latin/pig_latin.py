"""Exercism Python: Pig Latin"""


VOWELS = ["a", "e", "i", "o", "u"]


def get_cluster(word: str) -> str:
    """Returns the consonant cluster of a word
    word(str): word is a string
    """
    cluster = ""
    for char in word:
        # for cases of "y"
        if char == "y" and word[0] != "y":
            break

        elif char not in VOWELS:
            cluster += char

        # for cases of "qu"
        elif cluster[-1] == "q" and char == "u":
            cluster += char

        else:
            break

    return cluster


def begins_with_vowel_sound(word):
    """Returns true if word starts with a vowel sound. False otherwise."""

    # case of "xr" and "yt"
    if len(word) >= 2:
        first_letter, second_letter = word[0], word[1]
        pair = first_letter + second_letter
        if pair == "xr" or pair == "yt":
            return True

    return word[0] in VOWELS


def translate_word(text):
    """Translates an english word and returns the pig latin translation."""
    result_text = ""
    if begins_with_vowel_sound(text):
        result_text = text + "ay"

    # does not begin with vowel
    else:
        # get consonant cluster
        cluster = get_cluster(text)
        remaining_text = text[len(cluster) :]
        result_text = remaining_text + cluster + "ay"

    return result_text


def translate(text: str) -> str:
    """Translates a string text from english to pig latin.
    text(str): an english text

    Returns (str): pig latin string
    """

    words = [translate_word(word) for word in text.split(" ")]
    return " ".join(words)
