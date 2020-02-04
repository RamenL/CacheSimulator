from Set import Set
HEXA = 16
BIN = 2
REMOVE0B = 2
NUM_OF_BITS = 24
BEGINNING = 0
ZERO_HITS = 0

def find_address_tag(address, tag_amount):
    address_i = str(int(address, HEXA))
    binary = bin(int(address_i))[REMOVE0B:].zfill(NUM_OF_BITS)   # address in bits, including prepending zeroes
    tag_binary = binary[BEGINNING:tag_amount]
    return int(tag_binary, BIN)

class Cache():
    def __init__(self, cache_size, set_size, tag_amount, methodology):
        self.cache_size = cache_size
        self.set_size = set_size
        self.tag_amount = tag_amount
        self.cache_map = {}
        self.num_of_hits = ZERO_HITS
        self.methodology = methodology
        for x in range(cache_size):
            self.cache_map[x] = Set(set_size, x, methodology)

    def insert(self, address):
        tag = find_address_tag(address, self.tag_amount)
        set = self.cache_map[tag]
        self.num_of_hits += set.insert(address)

    def cache_print(self):
        for x in self.cache_map:
            print("Set " + str(x) + ": " + self.cache_map[x].set_print())
