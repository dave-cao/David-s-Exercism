"""Exercism Python: Perfect Numbers.

Problem:
    - Determine if a number is perfect, abundant, or deficient based on
        Nicomachus' classification scheme for positive integers.
    - Devised using the aliquot sum
        - defined as the sum of the factors of a number not including the number
            itself.
    - Perfect: aliquot sum = number
    - Abundant: aliquot sum > number
    - Deficient: aliquot sum < number
"""


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot = sum(i for i in range(1, number) if not number % i)
    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
