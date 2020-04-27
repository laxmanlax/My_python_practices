"""
Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
"""

def buddyString(A, B):
    if len(A)!=len(B):
        return False 
    
    if A==B and len(set(A)) < len(A):
        return True

    diff = [(a,b) for a,b in zip(A,B) if a!=b]
    if len(diff) == 2 and diff[0]==diff[1][::-1]:
        return True

A = "aaaaaaabc", B = "aaaaaaacb"
print buddyString(A, B)
