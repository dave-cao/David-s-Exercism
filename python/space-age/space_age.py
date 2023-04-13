"""Exercism Python: Space Age.

Problem:
    - Given an age in seconds, calculate how old someone would be on:
        - Mercury: orbital period 0.2408467 Earth years
        - Venus: orbital period 0.61519726 Earth years
        - Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
        - Mars: orbital period 1.8808158 Earth years
        - Jupiter: orbital period 11.862615 Earth years
        - Saturn: orbital period 29.447498 Earth years
        - Uranus: orbital period 84.016846 Earth years
        - Neptune: orbital period 164.79132 Earth years

Plan:
    - Convert seconds into Earth years, then convert from earth years to other
        planets
    - 1 earth year == 1/164 Neptune years.
"""


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = self.seconds / 31557600
        self.planets = {
            "neptune": 164.79132,
            "uranus": 84.016846,
            "saturn": 29.447498,
            "jupiter": 11.862615,
            "mars": 1.8808158,
            "venus": 0.61519726,
            "mercury": 0.2408467,
        }

    def on_earth(self):
        return round(self.earth_years, 2)

    def on_mercury(self):
        return round(self.earth_years / self.planets["mercury"], 2)

    def on_venus(self):
        return round(self.earth_years / self.planets["venus"], 2)

    def on_mars(self):
        return round(self.earth_years / self.planets["mars"], 2)

    def on_jupiter(self):
        return round(self.earth_years / self.planets["jupiter"], 2)

    def on_saturn(self):
        return round(self.earth_years / self.planets["saturn"], 2)

    def on_uranus(self):
        return round(self.earth_years / self.planets["uranus"], 2)

    def on_neptune(self):
        return round(self.earth_years / self.planets["neptune"], 2)
