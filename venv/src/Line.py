#Line has Address, Tag Value
class Line():
    def __init__(self, address, tag_amount):
        self.address = address
        #convert address to bits, then take the first tag_amount bits then save
        address_i = str(int(address, 16))
        num_of_bits = 24
        binary = bin(int(address_i, 16))[2:].zfill(num_of_bits) #address in bits, including prepending zeroes
        tag_binary = binary[0:tag_amount]
        self.tag_value = int(tag_binary, 2) #in decimal
        
