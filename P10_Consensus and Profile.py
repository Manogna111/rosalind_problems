#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

#Read the FASTA file
fasta_file = "/Users/manog/Downloads/fall_24 proj/data_practice/rosalind_cons.txt"
# Initialize a dictionary to store the sequences
sequences = {}

# Open and read the file
with open(fasta_file, 'r') as file:
    identifier = None
    sequence = []
    
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if identifier:
                sequences[identifier] = ''.join(sequence)
            identifier = line[1:]
            sequence = []
        else:
            sequence.append(line)
    
    # Don't forget to add the last sequence
    if identifier:
        sequences[identifier] = ''.join(sequence)

# Print the sequences in the desired format
import numpy as np
sequence_length = len(next(iter(sequences.values())))

profile = {
    'A': [0] * sequence_length,
    'C': [0] * sequence_length,
    'G': [0] * sequence_length,
    'T': [0] * sequence_length
}

for seq in sequences.values():
    for i, nucleotide in enumerate(seq):
        profile[nucleotide][i] += 1


    
consensus=''
for j in range(sequence_length):
    col_count = {
        'A': profile['A'][j],
        'C': profile['C'][j],
        'T': profile['T'][j],
        'G': profile['G'][j]
    }
    letter = max(col_count, key=col_count.get)
    consensus += letter
print(consensus)
for key in profile:
    counts = profile[key]
    print(key + ":", ' '.join(str(num) for num in counts))