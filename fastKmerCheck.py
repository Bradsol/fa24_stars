import sys
import ahocorasick

if len(sys.argv) < 4:
    print("Usage: python file.py <signal_gene_file> <genome_file> <output_kmer_file>")
    sys.exit(1)

signal_gene_input = sys.argv[1]
genome_input = sys.argv[2]
output_kmer_input = sys.argv[3]


def create_kmers(sequence, k): 
    kmers = []
    for i in range(len(sequence) - k + 1): # you can only make length - k + 1 kmers 
        kmers.append(sequence[i:i+k]) # add kmer to the list 
    return kmers

 
#FILE WE WANT KMERS OF
with open(signal_gene_input, 'r') as kras_file:
    text_kras = kras_file.read().replace('\n', '')  #removes the \n 



k = 50
# creating kmer of kras 
kmers = create_kmers(text_kras, k)
#creating dictionary
total_kmer_counts = {kmer: 0 for kmer in kmers}

# create Aho-Corasick automaton and add k-mers
A = ahocorasick.Automaton() # A will hold all the kmers to search for
for kmer in kmers:
    if kmer not in A:
        A.add_word(kmer, kmer)
A.make_automaton() # finalizes with checkpoints (will skip when partial matches fail)

# Search for k-mers in each line of the genome file
with open(genome_input, 'r') as cleanGenome:
      # specified length of Kmer
    num = 1
    
    for line in cleanGenome:
        line = line.strip()
        for end_index, kmer in A.iter(line): #find all occurances of kmer in line
            total_kmer_counts[kmer] += 1
        num += 1
        print(num)  # Track progress

#OPEN OUTPUT FILE and write each kmer and count to the file 
with open(output_kmer_input, 'w') as output_file:
    for kmer, count in total_kmer_counts.items():
        output_file.write(f"{kmer}: {count}\n")




