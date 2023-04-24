"""Exercism Python3: House

Problem:
- Recite the nursery rhyme 'This is the House that Jack Built' using
    recursion.
"""
import re

VERSES = [
    "that lay in the house that Jack built.",
    "that ate the malt",
    "that killed the rat",
    "that worried the cat",
    "that tossed the dog",
    "that milked the cow with the crumpled horn",
    "that kissed the maiden all forlorn",
    "that married the man all tattered and torn",
    "that woke the priest all shaven and shorn",
    "that kept the rooster that crowed in the morn",
    "that belonged to the farmer sowing his corn",
    "This is the horse and the hound and the horn",
]


def recurse(start_verse, end_verse):
    if start_verse == end_verse:
        VERSES[start_verse - 1] = re.sub(
            ".*the", "This is the", VERSES[start_verse - 1]
        )

    verse = VERSES[start_verse - 1]

    # base case
    if start_verse == 1:
        return verse
    else:
        return f"{verse} {recurse(start_verse - 1, end_verse)}"


def recite(start_verse, end_verse):
    return [recurse(i, i) for i in range(start_verse, end_verse + 1)]


print(recite(2, 4))
