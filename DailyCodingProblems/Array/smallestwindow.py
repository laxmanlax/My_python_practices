"""
Locate smallest window to be sorted in order to make the entire array to be sorted
Example : [3,7,5,6,9]  result -->> (1,3)
"""

"""
# Solution 1
def window(array):
    left , right = None, None
    sortedarry = sorted(array)
    for i in range(len(array)):
        if sortedarry[i] != array[i] and left is None:
            left = i
        elif sortedarry[i] != array[i]:
            right = i

    return left, right

"""

def window(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, array[i])

        if array[i] < max_seen:
            right = i

    for i in range(n-1, -1, -1):
        min_seen = min(min_seen, array[i])
        if array[i] > min_seen:
            left = i

    return left , right




array = [3,7,5,6,9]
print window(array)
