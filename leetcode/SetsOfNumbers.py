"""
find the no of subsets that sum up to a total value 
"""
def count_sets(arr, total):
    return rec(arr, total, len(arr) - 1, mem)

def rec(arr, total, i, mem):
    key = str(total)
    if key in mem:
        return mem[key]

    if total == 0:
        return 1
    elif total < 0:
        return 0 
    elif i < 0:
        return 0 
    elif total < arr[i]:
        to_return = rec(arr, total, i-1, mem)
    else:
        to_return = rec(arr, total - arr[i], i-1, mem) + rec(arr, total, i-1, mem)
    mem[key] = to_return
    return to_return



arr=[2,4,6,10]
total = 16   
print count_sets(arr, total)
 
