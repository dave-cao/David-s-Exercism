"""Exercism Python: Darts.

Problem:
    - Write a function that returns the earned points in a single toss of a Darts game
    - circle radius:
        - outer circle: 10 units --> 1 point
        - middle circle: 5 units --> 5 points
        - inner circle: 1 unit   --> 10 points

    - No points are given outside of the circle
"""

from math import sqrt


def score(x: float, y: float) -> int:
    """Calculate the score of a single toss of a Darts game.

    Params:
        x(float): x coordinate of the dart
        y(float): y coordinate of the dart

    Returns:
        score(int): the amount of points that was earned from the dart toss.
    """

    # list of tuples of (radius, score_awarded)
    point_system = [(1, 10), (5, 5), (10, 1)]

    for radius, score_awarded in point_system:
        if point_within_circle(x, y, radius):
            return score_awarded
    return 0


def point_within_circle(x: float, y: float, radius: int) -> bool:
    """Determines if a point coordinate is within a circle.

    Params:
        x(float): x coordinate of the point.
        y(float): y coordainte of the point
        radius(int): the radius of the circle from the origin

    Returns:
        bool: whether the point is within the circle or not.
    """
    return sqrt((x**2) + (y**2)) <= radius
