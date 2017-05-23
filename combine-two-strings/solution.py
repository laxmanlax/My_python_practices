class Two_string:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def combine(self):
        sufll = ''.join(sorted(self.c))
        if sufll[0:len(self.a)] in sufll and sufll[len(self.b):] in sufll:
            return True

tr = Two_string("abc", "def", "dfabde")
print tr.combine()
