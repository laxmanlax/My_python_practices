"""
Given a string S, find the longest palindromic substring in S.
Substring of string S:

S[i...j] where 0 <= i <= j < len(S)
Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :
Input : "aaaabaaa"
Output : "aaabaaa"
"""

def longestPalindromSub(S):
    maxl = ""
    for i in range(len(S)):
        lps = helperlps(S, i, i)
        if len(lps) > len(maxl):
            maxl = lps 

        lps = helperlps(S,i, i+1)
        if len(lps) > len(maxl):
            maxl = lps 
    return lps 

def helperlps(S, left, right):
    while left >= 0 and right <=len(S) and S[left]==S[right]:
        left -=1
        right +=1
    return S[left+1:right]

s = "aaaabaaa"
print longestPalindromSub(S)



