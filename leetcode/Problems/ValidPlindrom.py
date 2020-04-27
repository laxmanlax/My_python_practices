"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""
def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    for i in range(len(s)):
        tt = s[0:i]+s[i+1:]
        if tt == tt[::-1]:
            return True
    return False
