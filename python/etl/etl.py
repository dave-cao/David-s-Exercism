"""Exericsm Python: ETL

Problem:
    - Given legacy scrabble data, transform it to the shiny new format
    - The legacy data stored a list of letters per score (dictionary with lists)
    - the new format stores the score per letter (dictionary with ints)
"""


def transform(legacy_data: dict) -> dict:
    """Takes scrabble legacy data and formats it into the new scrabble scoring format.

    Params:
        - legacy_data(dict): A dictionary with the point as keys and list of letters
            as values.
    Returns:
        - new_data(dict): A dictionary with the letter as keys and point as values.
    """
    new_data = {}
    for point, letters in legacy_data.items():
        for letter in letters:  # create a key for each individual letter
            new_data[letter.lower()] = point

    return new_data
