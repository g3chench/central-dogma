from sys import *

def codons_to_letter(c):
    """Converts codon to amino acid.

    Args:
        c (str) -- 3-letter codon

    Returns:
        str -- the 1-letter abbreviation of the corresponding amino acid
    """

    return MAPPING2[MAPPING[c]]


# maps codons to amino acids
MAPPING = {
    'UUU': 'phenylalanine',
    'UUC': 'phenylalanine',
    'UUA': 'leucine',
    'UUG': 'leucine',

    'CUU': 'leucine',
    'CUC': 'leucine',
    'CUA': 'leucine',
    'CUG': 'leucine',

    'AUU': 'isoleucine',
    'AUC': 'isoleucine',
    'AUA': 'isoleucine',
    'AUG': 'START',

    'GUU': 'valine',
    'GUC': 'valine',
    'GUA': 'valine',
    'GUG': 'valine',

    'UCU': 'serine',
    'UCC': 'serine',
    'UCA': 'serine',
    'UCG': 'serine',

    'CCU': 'proline',
    'CCC': 'proline',
    'CCA': 'proline',
    'CCG': 'proline',

    'ACU': 'threonine',
    'ACC': 'threonine',
    'ACA': 'threonine',
    'ACG': 'threonine',

    'GCU': 'alanine',
    'GCC': 'alanine',
    'GCA': 'alanine',
    'GCG': 'alanine',

    'UAU': 'tyrosine',
    'UAC': 'tyrosine',
    'UAA': 'STOP',
    'UAG': 'STOP',

    'CAU': 'histidine',
    'CAC': 'histidine',
    'CAA': 'glutamine',
    'CAG': 'glutamine',

    'AAU': 'asparagine',
    'AAC': 'asparagine',
    'AAA': 'lysine',
    'AAG': 'lysine',

    'GAU': 'aspartic acid',
    'GAC': 'aspartic acid',
    'GAA': 'glutamic acid',
    'GAG': 'glutamic acid',

    'UGU': 'cysteine',
    'UGC': 'cysteine',
    'UGA': 'STOP',
    'UGG': 'tryptophan',

    'CGU': 'arginine',
    'CGC': 'arginine',
    'CGA': 'arginine',
    'CGG': 'arginine',

    'AGU': 'serine',
    'AGC': 'serine',
    'AGA': 'arginine',
    'AGG': 'arginine',

    'GGU': 'glycine',
    'GGC': 'glycine',
    'GGA': 'glycine',
    'GGG': 'glycine'
}


# maps amino acids to their abbreviations
MAPPING2 = {
    'phenylalanine': 'F',
    'leucine': 'L',
    'isoleucine': 'I',
    'START': 'M',
    'valine': 'V',
    'serine': 'S',
    'proline': 'P',
    'threonine': 'T',
    'alanine': 'A',
    'tyrosine': 'Y',
    'STOP': '?',
    'histidine': 'H',
    'glutamine': 'Q',
    'asparagine': 'N',
    'lysine': 'K',
    'aspartic acid': 'D',
    'glutamic acid': 'E',
    'cysteine': 'C',
    'tryptophan': 'W',
    'arginine': 'R',
    'glycine': 'G'
}


seq = argv[1]

rna = ''
rna = seq.replace('T', 'U')

output = ''
start = rna.index('AUG')
i = start

while (True):
    codon = rna[i:i+3]
    if len(codon) < 3:
        if ('AUG' in rna[start+1:]):    # reached end of sequence
            output = ''
            start = rna.index('AUG', start+1)   # looks for next
            i = start                           # start codon
        else:
            break   # no more start codons

    else:
        output += codons_to_letter(codon)
        i += 3
        if codons_to_letter(codon) == '?':  # valid sequence
            break

print(output)
