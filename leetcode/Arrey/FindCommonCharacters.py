"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""

def commonChars(A):
    """
    :type A: List[str]
    :rtype: List[str]
    """
    tracker = "abcdefghijklmnopqrstuvwxyz"
    result = {}
    ans = []
    for c in tracker:
        status = False 
        count = []
        
        for word in A:
            if c in word:
                status = True
                count.append(word.count(c))
 
        
        result[c]=[status,count]
    
    for k,v in result.items():
        #print k,v[0],v[1]
        if v[0]==True and len(v[1])==3:
            cnt = min(v[1])
            for i in range(cnt):
                ans.append(k)
    
    print ans


input1 = ["bella","label","roller"]
input2 = ["cool","lock","cook"] 
print commonChars(input2)


