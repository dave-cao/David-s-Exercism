"""Exercism Python: Bob

Problem:
- determine what Bob will say depening on what is said to him.

1. Any question is responded with "Sure"
2. All capital letter inputs is responded with "Woah, chill out!"
3. Silence -> "Fine. Be that way!" (silence is None or whitespace)
4. Anything else -> "Whatever."
"""


def response(hey_bob: str) -> str:
    """Determines what Bob will say after talking to him.

    Params:
        - hey_bob(str): what Bob hears

    Returns:
        - reply(str): what Bob will say
    """
    # takes away all whitespace from response
    hey_bob = hey_bob.strip()

    # Bob recieves silence
    if not hey_bob:
        return "Fine. Be that way!"

    # Bob gets asked a question if yelling form
    elif hey_bob[-1] == "?":
        # Bob gets asked a question in yelling form
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."

    # Bob gets yelled at
    elif hey_bob.isupper():
        return "Whoa, chill out!"

    # Bob recieves any other response
    else:
        return "Whatever."
