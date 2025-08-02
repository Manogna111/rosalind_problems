#Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

#Return: The adjacency list corresponding to O3. You may return edges in any order.

import os

#Read the FASTA file
fasta_file = "/Users/manog/Downloads/fall_24 proj/data_practice/rosalind_grph.txt"

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
#check for overlap graphs

folder = "/Users/manog/Downloads/fall_24 proj/results"
os.makedirs(folder, exist_ok=True)

output_path = os.path.join(folder, "overlap_output.txt")

with open(output_path, "w") as f:
    
    for id1, seq1 in sequences.items():
        for id2, seq2 in sequences.items():
            if id1 == id2:
                continue  # Skip self-loops
            # Next: check suffix/prefix overlap
            if seq1[-3:] == seq2[:3]:
                print(f"{id1} {id2}")  # Edge from id1 to id2
                f.write(f"{id1} {id2}\n")
    f.write("Saved safely!\n")

                

