from Set import Set

set = Set(4, 0, "FIFO")

addresses = [0, 1, 2, 3, 4, 0, 4, 3, 6]

for i in addresses:
    set.insert(i)

print(set.set_print())