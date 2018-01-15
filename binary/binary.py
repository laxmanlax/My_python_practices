class Binary:

    @classmethod
    def from_decimal(cls, dcml):
        binary=''
        while (dcml/2 != 1):
            binary += str(dcml%2)
            dcml = dcml/2
            if dcml == 2:
                binary += "01"
        return binary

    @classmethod
    def from_binary(cls, binary):
        n=0
        for char in binary[::-1]:
            n *=2
            if char == '1':
                n += 1
        return n


print Binary.from_decimal(36)
print Binary.frmo_binary("001001")
