"""Exercism Python: Anagram

Problem:
    - An anagram is a rearrangement of letters to form a new word: for
        example "owns" is an anagram of "snow"
    - A word cannot be it's own anagram
    - make a function that tells if a word is an anagram of another
"""

from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> set[str]:
    """Find the anagrams of a word given a list of other words.

    Params:
        - word(str): the target word to find an anagram of
        - candidates(list): a list of words to select if it is an anagram.

    Returns:
        - anagrams(set): the anagrams of the target word
    """
    return {candidate for candidate in candidates if is_anagram(word, candidate)}


def is_anagram(word: str, candidate: str) -> bool:
    """Determines if a word is an anagram of another word"""

    # allows case insensitivity
    word = word.lower()
    candidate = candidate.lower()

    # a word cannot be an anagram of itself
    if word == candidate:
        return False

    target_word_count = count_letters(word)
    candidate_count = count_letters(candidate)
    return target_word_count == candidate_count


def count_letters(word: str) -> Counter[str]:
    """Counts the number of letters in a word and outputs it as a dictionary."""
    return Counter(word)
