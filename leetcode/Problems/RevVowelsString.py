"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
"""
def reverseVowels(s):
    stack1 = []
    stack2 = []


    for i in range(len(s)):
        if s[i].lower() in ["a","e","i","o","u"]:
            stack1.append(s[i])
            stack2.append(i)
            
    tstr=list(s)

    for i in stack2:
        tstr[i]=stack1.pop()
    
    return "".join(tstr)

s = "leetcode"
print reverseVowels(s) 



