#f(10, [3, 4, 5, 6, 7]) // [ [4, 6], [3, 7] ]

class Pair:
    def __init__(self, a, b):
        self.a =a
        self.b =b

    def find_pair(self):
        increment = 0
        all_add=[]

        for i in range(len(self.b)):
            increment +=1
            for j in range(len(self.b))[increment:]:
                if self.b[i] + self.b[j] == 10:
                    all_add.append([self.b[i], self.b[j]])

        return all_add
a = Pair(10,[3,4,5,6,7])

print a.find_pair()
