def all_subset(given_array):
    subset = ["" for i in range(len(given_array))]
    helper(given_array, subset, 0)

def helper(given_array, subset, i):
    if i == len(given_array):
        print subset
    else:
        subset[i]=""
        helper(given_array, subset, i+1)

        subset[i]=given_array[i]
        helper(given_array, subset,i+1)

given_array =[1,2]
all_subset(given_array)

""
""
def powerSet(orinal, newset):
    if orinal == []:
        return [newset]
    else:
        res = []

        for s in powerSet(orinal[1:], newset+[orinal[0]]):
            res.append(s)
        
        for s in powerSet(orinal[1:], newset):
            res.append(s)
    
    return res 


