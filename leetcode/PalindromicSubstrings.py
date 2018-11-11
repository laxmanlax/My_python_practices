"""
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""
def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        count += helper(s, i, i)
        count += helper(s, i, i+1)
    return count 

def helper(string , left, right):
    inter_count = 0
    while left >=0 and right < len(string) and string[left]==string[right]:
        inter_count +=1
        left -=1
        right +=1
    return inter_count




