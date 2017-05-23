class Anagram:
    count=0
    sol=[]
    def __init__(self,a,b):
        self.a =a
        self.b =b

    def verify(self):
        for i in range(len(self.a)):
            if ''.join(sorted(self.a[i:len(self.b)+i]))==''.join(sorted(self.b)):
                self.sol.append(self.a[i:len(self.b)+i])
        return self.sol

a = Anagram('AbrAcadAbRa', 'cAda')
print a.verify()
