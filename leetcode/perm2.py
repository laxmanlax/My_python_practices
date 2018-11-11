def perm(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i]+lst[i+1:]
            print "for", x , xs 
            for p in perm(xs):
                l.append([x]+p)
                print "result ------",[x]+p 
            
        return l 


def perm2(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i]+lst[i+1:]
            for p in perm2(xs):
                yield [x]+p


data = list("aab")

# for p in perm2(data):
#     print p 
# 
# print "-------------------------------"


for p in perm2(data):
    if  "".join(p) == "".join(p[::-1]):
        print p ,"--"
