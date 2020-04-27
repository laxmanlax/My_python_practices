def perm3(lst):
    if len(lst)==0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            sx = lst[:i]+lst[i+1:]

            for p in perm3(sx):
                l.append([x]+p)
        
        return l 



S = "cba"
T = "abcd"


for per  in perm3(list(T)): 
    if S in "".join(per):
        print "".join(per) 
