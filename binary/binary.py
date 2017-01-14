class Binary:

    @classmethod
    def to_decimal(cls, dcml):
        binary=''
        while (dcml/2 != 1):
            binary += str(dcml%2)
            dcml = dcml/2
            if dcml == 2:
                binary += "01"
        return binary

    @classmethod
    def to_binary(cls, binary):
        n=0
        for char in binary[::-1]:
            n *=2
            if char == '1':
                n += 1
        return n


print Binary.to_decimal(36)
print Binary.to_binary("001001")
