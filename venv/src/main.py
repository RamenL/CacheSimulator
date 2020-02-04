from Cache import Cache

trace_file = "TRACE1.DAT" #trace_file path
L=3
KN=64 #cache_size
K=2 #set_size
methodology = "FIFO" #LRU or FIFO

N = int(KN/K)
NEXT = 0
f=open(trace_file, "rb") # read file in binary format
binary_file = list(f.read())
stack = [] # stack to reverse binary -> address
queue = [] # store final addresses

def find_tag_amount(n): # find tag length from number of set (N)
    tag_table = {4:2, 8:3, 16:4, 32:5, 64:6, 128:7, 256:8} #refactor this
    return tag_table[n]

def format_byte(byte):
    if len(byte) == 3: #in case appending zero is deleted
        byte = "0" + byte[2:3]
    else:
        byte = byte[2:4]
    return byte

def stack_to_word(stack): #pops stack elements to format address
    word = ""
    while stack:
        byte = str(stack.pop())
        word = word + format_byte(byte)
    return word


for i in binary_file: # adds bytes to stack. When stack limit is reached, calls stack_to_word and resets stack
    stack.append(hex(i))
    if len(stack) == L:
        queue.append(stack_to_word(stack))
        stack = [] #reset to empty stack
f.close()

cache = Cache(N, K, find_tag_amount(N), methodology) # cache object

q_len = len(queue)
while queue:
    cache.insert(queue.pop(NEXT)) #insert into cache

cache.cache_print()
print("Miss Rate for " +  trace_file + " (Method: " + str(methodology) + ", KN:" + str(KN) + ", N: " + str(N) + "): " + str((q_len - cache.num_of_hits)/q_len))