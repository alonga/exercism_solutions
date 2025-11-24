def to_rna(dna_strand):
    """Return the RNA complement of a DNA strand."""
    complement = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    
    rna = []
    for nucleotide in dna_strand:
        rna.append(complement[nucleotide])
    return ''.join(rna)