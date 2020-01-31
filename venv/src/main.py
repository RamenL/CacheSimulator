from Line import Line

trace_file = "TRACE1.DAT"
f=open(trace_file, "rb")
binary_file = list(f.read())

stack = []
queue = []
L=3
N=32
K=2

def find_tag_amount(n):
    tag_table = {4:2, 8:3, 16:4, 32:5, 64:6, 128:7, 256:8} #refactor this
    return tag_table[n]

def format_byte(byte):
    if len(byte) == 3: #in case appending zero is deleted
        byte = "0" + byte[2:3]
    else:
        byte = byte[2:4]
    return byte

def stack_to_word(stack):
    word = ""
    while stack:
        byte = str(stack.pop())
        word = word + format_byte(byte)
    return word


for i in binary_file:
    stack.append(hex(i))
    if len(stack) == L:
        queue.append(stack_to_word(stack))
        stack = [] #reset stack
        #break
    #insert somewhere

f.close()

#need hashmap of mapping from n to its counterpart

line = Line(queue.pop(), find_tag_amount(N))
print(line.tag_value)
#q -> cache