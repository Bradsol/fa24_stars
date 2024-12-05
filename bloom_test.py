from kmerCheck import text_kras
from bloomFilter import BloomFilter


def extract_kmers(sequence, k=31):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append(sequence[i:i + k])
    return kmers

# Returns a combined Bloom filter containing all k-mers
def build_bloom_filter_for_sequence(sequence, k=31):
    kmers = extract_kmers(sequence, k) 
    filters = []
    
    # Create a Bloom filter for each k-mer
    for kmer in kmers:
        bf = BloomFilter(size=200)  
        bf.add(kmer)  
        filters.append(bf)
    
    # Combine all Bloom filters into one filter 
    combined_filter = BloomFilter.combine_filters(filters)
    
    return combined_filter


def check_text_with_filter(text_data, bloom_filter):
    """
    Check if each line in a string is useful based on the Bloom filter.

    Parameters:
    - text_data (str): The input text or sequence (not a file path).
    - bloom_filter (BloomFilter): The Bloom filter to check against.

    Returns:
    - A list of tuples with line content and its status ("Possibly in filter" or "Not in filter").
    """
    results = []
    
    for line in text_data.splitlines():
        line = line.strip()  
        
        # Check if the line is in the Bloom filter
        if bloom_filter.check(line):  
            results.append((line, "Possibly in filter"))
        else:
            results.append((line, "Not in filter"))
    
    return results

k = 5  
combined_filter = build_bloom_filter_for_sequence(text_kras, k)

# Check specific k-mers or subsequences in the text_kras
test_sequence = """
ATGAG
GAGGA
ACTGA
XYZ
"""

# Run the Bloom filter check on the test sequence
results = check_text_with_filter(test_sequence, combined_filter)

# Print results
for text, status in results:
    print(f"{text}: {status}")