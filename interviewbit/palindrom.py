"""
You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
"""

def palindrom(tt):
    index1 = 0
    for i in range(1,len(tt)+1):
        if tt[0:i] == tt[0:i][::-1]:
            temp = tt[0:i]
            index1 = i 

    result = tt[index1:][::-1]+tt
    if result==result[::-1]:
        return len(tt[index1:])
       
s1 = "AACECAAAA"
s2 = "ABC"
s3 = "babb"
s4 = "apple"

print palindrom(s4)


