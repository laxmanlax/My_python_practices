"""
Subarrya SUM
"""

def max_subarrysum(array):
    current_max = 0
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            current_max = max(current_max, sum(array[i:j]))
    return current_max

def max_subarrysum(array):
    max_end_here , max_so_far = array[0]

    for i in range(1,len(A)-1):
        max_current = max(A[i] , max_current + A[i])
        if max_current > max_global:
            max_global = max_current

    return max_global


array = [34, -50, 42, 14, -5, 86]
print max_subarrysum(array)
