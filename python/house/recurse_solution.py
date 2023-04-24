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


def chant_verse(current_verse: int, beginning_verse: int) -> str:
    """Recite the current numbered verse all the way to the end."""
    verse = VERSES[current_verse - 1]  # -1 because we start at 0

    if current_verse == beginning_verse:
        # lazy matching
        verse = re.sub("^.*?the", "This is the", VERSES[current_verse - 1])

    # base case
    if current_verse == 1:
        return verse
    else:
        return f"{verse} {chant_verse(current_verse - 1, beginning_verse)}"


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the nursery rhyme 'This is the House that Jack Built'"""
    return [chant_verse(i, i) for i in range(start_verse, end_verse + 1)]
