START_CODE = 'AUG'
STOP_MARKER = object()
PROTEINS = {
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UAA': STOP_MARKER,
    'UAG': STOP_MARKER,
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGA': STOP_MARKER,
    'UGG': 'Tryptophan',
    'CUU': 'Leucine',
    'CUC': 'Leucine',
    'CUA': 'Leucine',
    'CUG': 'Leucine',
    'CCU': 'Proline',
    'CCC': 'Proline',
    'CCA': 'Proline',
    'CCG': 'Proline',
    'CAU': 'Histidine',
    'CAC': 'Histidine',
    'CAA': 'Glutamine',
    'CAG': 'Glutamine',
    'CGU': 'Arginine',
    'CGC': 'Arginine',
    'CGA': 'Arginine',
    'CGG': 'Arginine',
    'AUU': 'Isoleucine',
    'AUC': 'Isoleucine',
    'AUA': 'Isoleucine',
    'AUG': 'Methionine',
    'ACU': 'Threonine',
    'ACC': 'Threonine',
    'ACA': 'Threonine',
    'ACG': 'Threonine',
    'AAU': 'Asparagine',
    'AAC': 'Histidine',
    'AAA': 'Lysine',
    'AAG': 'Lysine',
    'AGU': 'Serine',
    'AGC': 'Serine',
    'AGA': 'Arginine',
    'AGG': 'Arginine',
    'GUU': 'Valine',
    'GUC': 'Valine',
    'GUA': 'Valine',
    'GUG': 'Valine',
    'GCU': 'Alanine',
    'GCC': 'Alanine',
    'GCA': 'Alanine',
    'GCG': 'Alanine',
    'GAU': 'Aspartic acid',
    'GAC': 'Aspartic acid',
    'GAA': 'Glutamic acid',
    'GAG': 'Glutamic acid',
    'GGU': 'Glycine',
    'GGC': 'Glycine',
    'GGA': 'Glycine',
    'GGG': 'Glycine',
}


def to_proteins(mRNA: str) -> list:
    mRNA = mRNA.upper()
    index = mRNA.find(START_CODE)
    if index == -1:
        return []
    proteins = []
    while index < len(mRNA):
        protein_key = mRNA[index:index + 3]
        protein = PROTEINS[protein_key]
        if protein == STOP_MARKER:
            break
        proteins.append(protein)
        index += 3
    return proteins


if __name__ == '__main__':
    strand = input('enter mRNA strand: ')
    direction = input('enter direction (right or left): ')
    if direction == 'left':
        strand = strand[::-1]
    elif direction == 'right':
        pass
    else:
        raise ValueError('was passed %s as a direction' % direction)
    proteins = to_proteins(strand)
    print(', '.join(proteins) if proteins else 'No Proteins found')
