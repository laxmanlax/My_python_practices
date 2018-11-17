"""
Input
    ABEC
    
Output
    6
Explanation
	Amazing substrings of given string are :
	1. A
	2. AB
	3. ABE
	4. ABEC
	5. E
	6. EC
	here number of substrings are 6 and 6 % 10003 = 6.
"""

def solve(A):
    sum = 0
    for x in range(len(A)):
        if A[x] in "AEIOUaeiou":
            sum = sum+len(A)-x

    sum = sum % 10003
    return sum

a="ABEC"
print solve(a)