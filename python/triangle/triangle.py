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


def is_triangle(sides: list[int]) -> bool:
    """Checks to see if 3 lengths can possibly be a triangle"""
    sides = sorted(sides)
    return all(sides) and sum(sides[:2]) >= sides[2]


def equilateral(sides: list[int]) -> bool:
    """All sides are the same"""
    return is_triangle(sides) and all(side == sides[0] for side in sides)


def isosceles(sides: list[int]) -> bool:
    """At least two sides are the same length."""
    return is_triangle(sides) and bool(
        {side for side in sides if sides.count(side) > 1}
    )


def scalene(sides: list[int]) -> bool:
    """All sides are different lengths"""
    return is_triangle(sides) and len(set(sides)) == 3
