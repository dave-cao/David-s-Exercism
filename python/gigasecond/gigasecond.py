"""Exercism Python: Gigasecond.

Problem:
    - Determine the date and time of one gigasecond after a certain date
    - 1 000 000 000 seconds
"""

from datetime import datetime, timedelta

def add(moment: datetime) -> datetime:
    """Add a gigasecond to any given moment"""
    GIGASECOND = timedelta(0, 1000000000)
    return moment + GIGASECOND

