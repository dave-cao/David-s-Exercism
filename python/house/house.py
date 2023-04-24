"""Exercism Python3: House

Problem:
- Recite the nursery rhyme 'This is the House that Jack Built' using
    recursion.
"""

VERSES = [
    "the house that Jack built.",
    "the malt that lay in ",
    "the rat that ate ",
    "the cat that killed ",
    "the dog that worried ",
    "the cow with the crumpled horn that tossed ",
    "the maiden all forlorn that milked ",
    "the man all tattered and torn that kissed ",
    "the priest all shaven and shorn that married ",
    "the rooster that crowed in the morn that woke ",
    "the farmer sowing his corn that kept ",
    "the horse and the hound and the horn that belonged to ",
]


def chant_verse(start_verse: int) -> str:
    """Recite the current numbered verse all the way to the end."""
    return "This is " + "".join([VERSES[i] for i in range(start_verse - 1, -1, -1)])


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the nursery rhyme 'This is the House that Jack Built'"""
    return [chant_verse(i) for i in range(start_verse, end_verse + 1)]
