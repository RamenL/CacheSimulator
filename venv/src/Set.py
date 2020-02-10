MISS = 0
HIT = 1
NEXT_ITEM = 0
LRU = "LRU"

class Set():
    def __init__(self, lines_per_set, tag, methodology):
        self.lines_per_set = lines_per_set
        self.tag = tag
        self.line_list = []
        self.methodology = methodology

    def insert(self, address):
        if len(self.line_list) < self.lines_per_set: #if cache not full yet
            self.line_list.append(address) #add to set
            return MISS
        else: ##LRU Implementation https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/
            if address in self.line_list: #check if exists, if so increase hit counter
                if self.methodology == LRU: # if LRU Method
                    self.line_list.remove(address) # remove from list
                    self.line_list.append(address) # append to end
                return HIT
            else:
                self.line_list.pop(NEXT_ITEM) #pop first item
                self.line_list.append(address)
                return MISS

    def set_print(self):
        set_address = ""
        for current in self.line_list:
            set_address = set_address + str(current) + ", "
        return set_address