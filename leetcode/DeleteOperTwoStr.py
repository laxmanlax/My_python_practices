"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you 
can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

********************************************************************************************
Because it can only do delete operations, this is actually the longest common subsequence problem.
Define dp[i][j] to represent the longest common subsequence length between word1[:i+1] and word2[:j+1]
The recursive formula is as follows:

Dp[i][j] = dp[i-1][j-1] + 1 if word1[i] == word2[j]
else 
Dp[i][j] = max(dp[i-1][j], dp[i][j-1])

The dp array in the example should look like this:

	e	a	t
s	0	0	0
e	1	1	1
a	1	2	2



Initialize all dp[0][j], dp[i][0]
Follow the recursive operation
Remember l = dp[-1][-1], 
then return m-l + n-l,m,n represent the length of word1 and word2 respectively
Processing data is empty
"""

def minDistance(A, B):
    M, N = len(A), len(B)
    dp = [[0] * (N+1) for _ in range(M+1)]
    print dp 

    for i in range(1, M+1):
        for j in range(1, N+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[M][N]

A=""
B="a"
print minDistance(A, B)
    

# A Naive recursive Python implementation of LCS problem
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1)
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"

print "Length of LCS is ", lcs(X, Y, len(X), len(Y))
