import sys

if len(sys.argv) < 4:
    print("Usage: python file.py <signal_gene_file> <genome_file> <output_kmer_file>")
    sys.exit(1)

signal_gene_input = sys.argv[1]
genome_input = sys.argv[2]
output_kmer_input = sys.argv[3]

# bloom Filter using geeksforgeeks and built in hash 
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size # set all bits to zero

    def add(self, item)
        for i in range(self.hash_count): # hashes multiple times 
            digest = (hash(item + str(i))) % self.size # maps to position within size - generate different hashes
            self.bit_array[digest] = 1 

    def check(self, item):
        for i in range(self.hash_count):
            digest = (hash(item + str(i))) % self.size #checks each position
            if self.bit_array[digest] == 0: # if ever zero - defintely not in bloom filter
                return False
        return True


def create_kmers(sequence, k):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

# initialize bloom
bloom_filter_size = 2000000 
hash_count = 2  # hash functions
bloom_filter = BloomFilter(bloom_filter_size, hash_count)

#loading kras 
with open(signal_gene_input, 'r') as kras_file:
    text_kras = kras_file.read().replace('\n', '')
    k = 6  # length of k-mer
    kmers = create_kmers(text_kras, k)
    for kmer in kmers:
        bloom_filter.add(kmer)

# # search genome for k-mers - count matches
# total_kmer_counts = {kmer: 0 for kmer in kmers}
# with open(genome_input, 'r') as cleanGenome:
#     num = 1
#     for line in cleanGenome:
#         if num > 50:  # limit lines for runtime
#             break

#         line = line.strip()
#         line_kmers = create_kmers(line, k)
        
#         for line_kmer in line_kmers:
#             if bloom_filter.check(line_kmer):
#                 if line_kmer in total_kmer_counts:
#                     total_kmer_counts[line_kmer] += 1

#         num += 1
#         print(f"Processed line: {num}")  # track runtime

# Write k-mer counts to output file
with open(output_kmer_input, 'w') as output_file:
    for kmer, count in total_kmer_counts.items():
        output_file.write(f"{kmer}: {count}\n")
