from itertools import groupby
def splt(l):
    t2=[]
    t3=[]
    for i,j in groupby(map(lambda x:(x[0],x[1]),tt),  lambda x:x[0]):
        t2.append(list(j))

    for i in [[''.join(row[i]) for row in t2] for i in range(4)]:
        t3.extend(i)
    return t3

tt = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4']
print splt(tt)
