"""Exercism Python: Anagram

Problem:
    - An anagram is a rearrangement of letters to form a new word: for
        example "owns" is an anagram of "snow"
    - A word cannot be it's own anagram
    - make a function that tells if a word is an anagram of another
"""


def find_anagrams(word: str, candidates: list) -> set:
    """Find the anagrams of a word given a list of other words.

    Params:
        - word(str): the target word to find an anagram of
        - candidates(list): a list of words to select if it is an anagram.

    Returns:
        - anagrams(set): the anagrams of the target word
    """

    anagrams = set()
    for candidate in candidates:
        if is_anagram(word, candidate):
            anagrams.add(candidate)

    return anagrams


def is_anagram(word: str, candidate: str) -> bool:
    """Determines if a word is an anagram of another word"""

    # a word cannot be an anagram of itself
    if word.lower() == candidate.lower():
        return False

    target_word_count = count_letters(word)
    candidate_count = count_letters(candidate)
    return target_word_count == candidate_count


def count_letters(word: str) -> dict:
    """Counts the number of letters in a word and outputs it as a dictionary."""
    word_count = {}
    for letter in word.lower():
        word_count[letter] = word_count.get(letter, 0) + 1
    return word_count
