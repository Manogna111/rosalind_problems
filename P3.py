'''
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s
.
'''

#Dictionary
def reverse_complement(dna):

    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_dna = dna[::-1]
    reverse_complement = ''.join(complement[base] for base in reversed_dna)
    return reverse_complement

dna_s = input("Enter a DNA string (A, T, C, G): ").upper()
result  = reverse_complement(dna_s)
print(result)