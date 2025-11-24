def proteins(strand):
    codon_map = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine",       "UUG": "Leucine",
        "UCU": "Serine",        "UCC": "Serine",
        "UCA": "Serine",        "UCG": "Serine",
        "UAU": "Tyrosine",      "UAC": "Tyrosine",
        "UGU": "Cysteine",      "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
    }

    result = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        protein = codon_map.get(codon)
        if protein == "STOP":
            break
        if protein:  # ignore unknown codons
            result.append(protein)

    return result

