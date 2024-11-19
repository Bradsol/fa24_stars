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



k = 8
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






'''
import sys

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

def kmer_count(kmers, text, k): 
  kmer_counts = {} #create dictionary 

  for kmer in kmers: #iterates through kmer list, initializing every count to 0 
    kmer_counts[kmer] = 0

  for i in range(len(text) - k + 1): # goes through every possible substring of length of kmer
    subsequence = text[i:i+k] 
    if subsequence in kmer_counts: # if that substring is equal to a kmer in the list, increment the kmer count 
      kmer_counts[subsequence] += 1
  
  return kmer_counts

 
#FILE WE WANT KMERS OF
with open(signal_gene_input, 'r') as kras_file:
    text_kras = kras_file.read().replace('\n', '')  #removes the \n 


#FILE WE SEARCH FOR KMERS IN 
with open(genome_input, 'r') as cleanGenome:
    k = 8  # specified length of Kmer
    num = 1
    
    # creating kmer of kras 
    kmers = create_kmers(text_kras, k)
    total_kmer_counts = {kmer: 0 for kmer in kmers}

    # iterate over lines in cleanGenome.txt
    for line in cleanGenome: 

      # count k-mers in the current line of cleanGenome
      kmer_count_dict = kmer_count(kmers, line.strip(), k) 
      #print(f"Line {num}: {kmer_count_dict}")

      #add each line kmer count a total dictionary 
      for kmer, count in kmer_count_dict.items():
            total_kmer_counts[kmer] += count
      

      num += 1
      print(num) #track the lines


#OPEN OUTPUT FILE and write each kmer and count to the file 
with open(output_kmer_input, 'w') as output_file:
    for kmer, count in total_kmer_counts.items():
        output_file.write(f"{kmer}: {count}\n")


'''



# /*
# def create_kmers(sequence, k): 
#     kmers = []
#     for i in range(len(sequence) - k + 1): # you can only make length - k + 1 kmers 
#         kmers.append(sequence[i:i+k]) # add kmer to the list 
#     return kmers

# def kmer_count(kmers, text, k): 
#   kmer_counts = {} #create dictionary 

#   for kmer in kmers: #iterates through kmer list, initializing every count to 0 
#     kmer_counts[kmer] = 0

#   for i in range(len(text) - k + 1): 
#     subsequence = text[i:i+k]
#     if subsequence in kmer_counts:
#       kmer_counts[subsequence] += 1
  
#   return kmer_counts

# #open file 

# with open('fakeSequence.txt', 'r') as kras_file:
#     text_kras = kras_file.read().replace('\n', '')  #removes the \n 



# with open('testClean.txt', 'r') as cleanGenome:
#     k = 8  # specified length of Kmer
#     num = 1
    
#     # creating kmer of kras 
#     kmers = create_kmers(text_kras, k)
#     total_kmer_counts = {kmer: 0 for kmer in kmers}

#     # iterate over lines in cleanGenome.txt
#     for line in cleanGenome: 
#       #print(line)
#       if num > 200:  
#           break

#         # count k-mers in the current line of cleanGenome
#       kmer_count_dict = kmer_count(kmers, line.strip(), k) 
#       print(f"Line {num}: {kmer_count_dict}")
#       num += 1
#       print(num)

#       for kmer, count in kmer_count_dict.items():
#             total_kmer_counts[kmer] += count

# # find the k-mer that occurred the most often
# most_frequent_kmer = max(total_kmer_counts, key=total_kmer_counts.get)
# most_frequent_count = total_kmer_counts[most_frequent_kmer]

# # print the most frequent k-mer and its count
# print(f"The most frequent k-mer is: {most_frequent_kmer} with a count of {most_frequent_count}")

# print("Total K-mer counts including zero counts:", total_kmer_counts)

# with open('testOutput.txt', 'w') as output_file:
#     for kmer, count in total_kmer_counts.items():
#         output_file.write(f"{kmer}: {count}\n")




