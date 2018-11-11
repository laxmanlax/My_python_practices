"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

import re 
def reverseOnlyLetters(S):
    """
    :type S: str
    :rtype: str
    """
    stack1 = []
    stack2 = []
    
    for i in range(len(S)):
        if not S[i].isalpha():
            stack1.append(i)
            stack2.append(S[i])

    rev_list = list("".join(re.split("[\W+\d*]", S[::-1])))

    for i in range(len(stack1)):
        rev_list.insert(stack1[i], stack2[i])

    return "".join(rev_list)


S = "ab-cd"
print reverseOnlyLetters(S) == "dc-ba"

S = "a-bC-dEf-ghIj"
print reverseOnlyLetters(S) == "j-Ih-gfE-dCba"

S = "Test1ng-Leet=code-Q!"
print reverseOnlyLetters(S)=="Qedo1ct-eeLg=ntse-T!"
