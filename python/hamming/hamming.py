"""Exercism Python: Hamming.

The hamming distance is the amount of differences between two different DNA

"""


def distance(strand_a, strand_b):
    """Given strand_a and strand_b, caluclates the hamming distance between the two."""

    # Error if strands are not equal length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming = 0
    for i, letter in enumerate(strand_a):  # compare strand_a wtih strand_b
        if letter != strand_b[i]:
            hamming += 1
    return hamming
