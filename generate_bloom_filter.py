## implementation with new calculations
## want 5 hash functions, 2000000 bits, 45635 elements, fpr = 0.000015

import random
import string
import sys

#define constants for our calculation
KMER_LENGTH = 50
BLOOM_SIZE = 2000000
NUM_HASH_FUNC = 6


def create_kmers(sequence, k):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]


class BloomFilter:
    #initialize Bloom Filter using the calculated metrics above
    def __init__(self, size=BLOOM_SIZE, num_hashes=NUM_HASH_FUNC):
        self.size = size
        self.num_hashes = num_hashes
        # set all 2 million to false 
        self.bit_array = [False] * size 

    #creates multiple hash functions (specified in constant above)
    def _hashes(self, item):
        return [(hash(str(i) + item) % self.size) for i in range(self.num_hashes)]

    #add items to bloom filter using our created hash functions
    def add(self, item):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = True  

    #check if the item/sequence could be in the Bloom Filter using the hash functions
    def check(self, item):
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))

    #combines multiple bloom filters 
    @staticmethod
    def combine_filters(filters):
        combined_filter = BloomFilter(filters[0].size, filters[0].num_hashes)
        for f in filters:
            combined_filter.bit_array = [x or y for x, y in zip(combined_filter.bit_array, f.bit_array)]
        return combined_filter

def process_dataset_to_bloom_filter(file_path, k=KMER_LENGTH, bf_size=BLOOM_SIZE, num_hashes=NUM_HASH_FUNC):
    #create bloom filter
    bf = BloomFilter(size=bf_size, num_hashes=num_hashes)

    # read sequence data from file
    with open(file_path, "r") as sequence_file:
        sequence_data = sequence_file.read().replace('\n', '')
        kmers = create_kmers(sequence_data, k)
        for kmer in kmers:
          bf.add(kmer)
    
    print(f"Processed {file_path} → Bloom filter with {k}-mers created.")
    return bf

def test_false_positive_rate(bf, num_inserted=45635, num_test=500000):
 
    inserted_items = set()
    while len(inserted_items) < num_inserted:
        inserted_items.add("".join(random.choices(string.ascii_uppercase, k=4)))

    for item in inserted_items:
        bf.add(item)

    not_included_items = set()
    while len(not_included_items) < num_test:
        new_item = "".join(random.choices(string.ascii_uppercase, k=4))
        if new_item not in inserted_items: 
            not_included_items.add(new_item)

    false_positives = sum(bf.check(item) for item in not_included_items)
    fpr = (false_positives / num_test) * 100  

    print(f"False Positives: {false_positives} out of {num_test} ({fpr:.4f}% FPR)")
    
    return fpr


# Run the test
if __name__ == "__main__":
  if len(sys.argv) < 2:
      print("Usage: python file.py <dataset1> <dataset2> ...")
      sys.exit(1)

  #place set paths into array
  dataset_paths = sys.argv[1:]

  # loop and process each dataset to create filters
  bloom_filters = {}
  for dataset in dataset_paths:
      bloom_filters[dataset] = process_dataset_to_bloom_filter(dataset)    

  KRAS = list(bloom_filters.keys())[0] 
  TP53 = list(bloom_filters.keys())[1] 
  EGFR = list(bloom_filters.keys())[2] 


  #expected output: 
  print(bloom_filters[KRAS].check('ABCD')) #false
  print(bloom_filters[KRAS].check('CTAGGCGGCGGCCGCGGCGGCGGAGGCAGCAGCGGCGGCGGCAGTGGCGG')) #true: exists in KRAS Filter 
  print(bloom_filters[TP53].check('TGCATTGTTGGGAGACCTGGGTGTAGATGATGGGGATGTTAGGACCATCC')) #true: exists in TP53 Filter 
  print(bloom_filters[EGFR].check('CCGCCCTCCGCGCAGGTCTCAAACTGAAGCCGGCGCCCGCCAGCCTGGCC')) #true: exists in EGFR Filter 

  print(f"All {len(bloom_filters)} datasets have been converted into Bloom filters!")
