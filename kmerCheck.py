
def create_kmers(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append(sequence[i:i+k])
    return kmers

def kmer_count(kmers, text, k): 
  kmer_counts = {}

  for kmer in kmers:
    kmer_counts[kmer] = 0

  for i in range(len(text) - k + 1):
    subsequence = text[i:i+k]
    if subsequence in kmer_counts:
      kmer_counts[subsequence] += 1
  
  return kmer_counts

#open file 

with open('KRAS.txt', 'r') as kras_file:
    text_kras = kras_file.read().replace('\n', '')  #removes the \n 



with open('cleanGenome.txt', 'r') as cleanGenome:
    k = 50  # Length of k-mers
    num = 1
    
    # Create k-mers from the KRAS sequence
    kmers = create_kmers(text_kras, k)
    total_kmer_counts = {kmer: 0 for kmer in kmers}

    # Iterate over lines in cleanGenome.txt
    for line in cleanGenome: 
      #print(line)
      if num > 100000:  # You only want to read the first line based on your original code
          break

        # Count k-mers in the current line of cleanGenome
      kmer_count_dict = kmer_count(kmers, line.strip(), k)  # Strip whitespace/newline characters
      #print(f"Line {num}: {kmer_count_dict}")
      num += 1
      print(num)

      for kmer, count in kmer_count_dict.items():
            total_kmer_counts[kmer] += count

# Find the k-mer that occurred the most often
most_frequent_kmer = max(total_kmer_counts, key=total_kmer_counts.get)
most_frequent_count = total_kmer_counts[most_frequent_kmer]

# Print the most frequent k-mer and its count
print(f"The most frequent k-mer is: {most_frequent_kmer} with a count of {most_frequent_count}")









# k = 50
# num = 1
# kmers = create_kmers(text_kras, k)

# for line in cleanGenome: 
#   if num > 1:
#     break

#   kmer_count_dict = kmer_count(kmers, line, k)
#   print(f"Line {num}: {kmer_count_dict}")
#   num = num + 1
  









