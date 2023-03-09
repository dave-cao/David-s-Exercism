"""Exercism Python: RNA Transaction

Problem:
    - Given a strand of DNA, give back its RNA complement
"""


def to_rna(dna_strand: str) -> str:
    """Return the RNA complement to the DNA strand given.

    Params:
        - dna_strand(str): the DNA strand

    Returns:
        - rna_strand(str): the RNA strand complement to the DNA
    """

    # Dictionary containing DNA and its complements
    dna_complements = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    rna_strand = ""
    for nucleotide in dna_strand:
        rna_strand += dna_complements[nucleotide]

    return rna_strand
