"""Exercism Python: Wordy

Problem:
    - We are given a equation but its in string form. We need to comprehend it,
        and then output an integer answer.
    - There can be two types of errors
        1. "unknown operation": There is no known operation within the string
            - if the str is "What is?" it does not count
        2. "syntax error": There is a known operation but it doesn't work.
            - "What is?" is considered a syntax error
"""

OPERATIONS = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "multiplied": lambda x, y: x * y,
    "divided": lambda x, y: x // y,
}


def answer(question: str) -> int:
    """Given a word equation, output its answer as an integer."""

    question = question[:-1]  # get rid of question mark at end of str
    question = question[8:]  # get rid of "What is " in front of str
    word_list = question.split(" ")

    # turn str numbers in numbers
    equation = [
        int(word) if word.lstrip("-").isnumeric() else word for word in word_list
    ]
    # get rid of the word "by"
    equation = [word for word in equation if word != "by"]

    # Checks to see if question has an unknown operation error
    operation_check = False
    for item in equation:
        if (
            item in OPERATIONS.keys()  # known operator in question
            or item == ""  # accounts for "What is?"
            or (len(equation) == 1 and type(equation[0] == int))  # "What is 5?" == 5
        ):
            operation_check = True
    if not operation_check:
        raise ValueError("unknown operation")

    result = equation[0]  # start on first number
    if not result:
        raise ValueError("syntax error")

    # calculate the string equation
    for i in range(1, len(equation), 2):  # we have to do this by 2
        try:
            operation_func = OPERATIONS[str(equation[i])]
            result = operation_func(result, equation[i + 1])
        except:
            raise ValueError("syntax error")

    return int(result)
