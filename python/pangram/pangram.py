"""Exercism Python: Pangram."""


def is_pangram(sentence):
    """Determines if a sentence is a pangram.

    A pangram is a sentence that uses every letter in the alphabet at least once.

    Params:
        sentence(str): a string that is given as input.

    """
    # initialize alphabet dictionary
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = {letter: 0 for letter in alphabet}

    # count the letters in sentence
    for letter in sentence.lower():
        if letter in alphabet:
            alphabet[letter] += 1

    # determine if every letter in alphabet was used
    for count in alphabet.values():
        if not count:
            return False
    return True
