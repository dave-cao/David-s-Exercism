"""Exercism Python: Wordy

Problem:
    - We are given a equation but its in string form. We need to comprehend it,
        and then output an integer answer.
"""

# Search up lambdas later


def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y




def answer(question: str) -> int:
    """Given a word equation, output its answer as an integer."""

    operations = {"plus": add, "minus": minus, "multiplied": multiply, "divided": divide}

    # Get rid of question mark from question and the "What is" part
    question = question[:-1]
    question = question[8:]

    # Seperate each word
    word_list = question.split(" ")

    # turn str numbers in numbers
    equation = [int(word) if word.lstrip("-").isnumeric() else word for word in word_list]
    equation = [word for word in equation if word != "by"] # how to combine this with above


    # calculate the string equation
    result = equation[0]
    for i in range(1, len(equation), 2):  # we have to do this by 2
        result = operations[equation[i]](result, equation[i + 1])


    print(result)
    return result


answer("What is -3 plus 7 multiplied by -2?")

# the problem now is negative numbers
