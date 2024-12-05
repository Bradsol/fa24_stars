# import math
# import mmh3
# from bitarray import bitarray


# class BloomFilter(object):

#     '''
#     Class for Bloom filter, using murmur3 hash function
#     '''

#     def __init__(self, items_count, fp_prob):
#         '''
#         items_count : int
#             Number of items expected to be stored in bloom filter
#         fp_prob : float
#             False Positive probability in decimal
#         '''
#         # False possible probability in decimal
#         self.fp_prob = fp_prob

#         # Size of bit array to use
#         self.size = self.get_size(items_count, fp_prob)

#         # number of hash functions to use
#         self.hash_count = self.get_hash_count(self.size, items_count)

#         # Bit array of given size
#         self.bit_array = bitarray(self.size)

#         # initialize all bits as 0
#         self.bit_array.setall(0)

#     def add(self, item):
#         '''
#         Add an item in the filter
#         '''
#         digests = []
#         for i in range(self.hash_count):

#             # create digest for given item.
#             # i work as seed to mmh3.hash() function
#             # With different seed, digest created is different
#             digest = mmh3.hash(item, i) % self.size
#             digests.append(digest)

#             # set the bit True in bit_array
#             self.bit_array[digest] = True

#     def check(self, item):
#         '''
#         Check for existence of an item in filter
#         '''
#         for i in range(self.hash_count):
#             digest = mmh3.hash(item, i) % self.size
#             if self.bit_array[digest] == False:

#                 # if any of bit is False then,its not present
#                 # in filter
#                 # else there is probability that it exist
#                 return False
#         return True

#     @classmethod
#     def get_size(self, n, p):
#         '''
#         Return the size of bit array(m) to used using
#         following formula
#         m = -(n * lg(p)) / (lg(2)^2)
#         n : int
#             number of items expected to be stored in filter
#         p : float
#             False Positive probability in decimal
#         '''
#         m = -(n * math.log(p))/(math.log(2)**2)
#         return int(m)

#     @classmethod
#     def get_hash_count(self, m, n):
#         '''
#         Return the hash function(k) to be used using
#         following formula
#         k = (m/n) * lg(2)

#         m : int
#             size of bit array
#         n : int
#             number of items expected to be stored in filter
#         '''
#         k = (m/n) * math.log(2)
#         return int(k)

class BloomFilter:
    def __init__(self, size=2000000):
        """Initialize Bloom Filter with a bit array of given size."""
        self.size = size
        self.bit_array = [False] * size

    def add(self, item):
        """Add an item to the Bloom Filter by hashing it."""
        hash_value = hash(item) % self.size  # Hash the item and get an index
        self.bit_array[hash_value] = True  # Set the corresponding bit to True

    def check(self, item):
        """Check if an item could be in the Bloom Filter."""
        hash_value = hash(item) % self.size  # Hash the item and get an index
        return self.bit_array[hash_value]  # Return whether the bit is set to True

    @staticmethod
    def combine_filters(filters):
        """Combine multiple Bloom filters by summing their bit arrays (bitwise OR)."""
        combined_filter = BloomFilter(filters[0].size)
        for f in filters:
            combined_filter.bit_array = [x or y for x, y in zip(combined_filter.bit_array, f.bit_array)]
        return combined_filter
