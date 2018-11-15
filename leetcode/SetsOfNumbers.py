"""
find the no of subsets that sum up to a total value 
"""

def count_sets(arr, total):
    return rec(arr, total, len(arr) - 1)

def rec(arr, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0 
    elif i < 0:
        return 0 
    elif total < arr[i]:
        print total , arr, arr[i]
        return rec(arr, total, i-1)
    else:
        print total, arr, arr[i]
        return rec(arr, total - arr[i], i-1) + rec(arr, total, i-1)


arr=[2,4,6,10]
total = 16   
print count_sets(arr, total)
 
