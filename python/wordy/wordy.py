"""Exercism Python: Wordy

Problem:
    - We are given a equation but its in string form. We need to comprehend it,
        and then output an integer answer.
"""

# Search up lambdas later


def add(x, y):
    return x + y


def answer(question: str) -> int:
    """Given a word equation, output its answer as an integer."""

    operations = {"plus": add}

    # Get rid of question mark from question and the "What is" part
    question = question[:-1]
    question = question[8:]

    # Seperate each word
    word_list = question.split(" ")

    # turn str numbers in numbers
    equation = [int(word) if word.isnumeric() else word for word in word_list]

    result = 0
    for i in range(0, len(equation), 3):  # we have to do this by 2
        print(i)
        # if i == 0:
        #     result = operations[equation[i + 1]](equation[i], equation[i + 2])
        # else:
        #     result = operations[equation[i]](result, equation[i + 1])

    # print(result)

    # result = operations[equation[1]](equation[0], equation[2])

    # print(result)


answer("What is 1 plus 1 plus 1 plus 1 plus 1?")
