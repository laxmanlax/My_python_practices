"""
Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.""
"""
def customSortString(S, T):
    for i in S:
        if i in T:
            if T.count(i) > 1:
                S=S.replace(i,i*T.count(i))
            
            T=T.replace(i,"")
        else:
            S=S.replace(i,"")
    
    return S+T


S = "cba"
T = "abcd"
print customSortString(S, T)
