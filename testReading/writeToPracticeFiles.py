import random

# Function to generate a random DNA sequence
def generate_sequence(length):
    return ''.join(random.choice('AGTC') for i in range(length))

# Generate the target sequence (KRAS sequence) that we want to search for
kras_sequence = generate_sequence(500)

# Generate a larger genome sequence with the KRAS sequence embedded
genome_sequence = generate_sequence(4000)  # Generate a random genome
# Insert the KRAS sequence at a random position
insert_position = random.randint(0, len(genome_sequence) - len(kras_sequence))
genome_sequence = genome_sequence[:insert_position] + kras_sequence + genome_sequence[insert_position + len(kras_sequence):]

# Write the KRAS sequence to KRAS.txt
with open('fakeSequence.txt', 'w') as kras_file:
    kras_file.write(kras_sequence)

# Write the genome sequence to cleanGenome.txt
with open('testClean.txt', 'w') as genome_file:
    # Split the genome into lines of 80 characters for easier reading
    for i in range(0, len(genome_sequence), 80):
        genome_file.write(genome_sequence[i:i+80] + '\n')

print("Test sequences have been generated.'")
