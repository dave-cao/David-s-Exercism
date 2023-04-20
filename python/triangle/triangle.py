"""Exercism Python: Triangle

Problem:
- Determine if a triangle is equilateral, isosceles, or scalene.

1. Equilateral: all three sides the same length
2. Isolsceles: at least two sides are the same length
3. Scalene: all sides are different length

Caveats: 
- for a shape to be a triangle, all sides must have a length > 0, and the sum
    of the lengths of any two sides must be greater than or equal to the
    length of the third side.
"""


def equilateral(sides: list[int]) -> bool:
    return all(side == sides[0] for side in sides)


def isosceles(sides):
    pass


def scalene(sides):
    pass


equilateral([3, 2, 2])
