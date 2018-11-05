def longestPalinDrom(s):
    res = ""
    for i in range(s):
        temp = helper(s, i, i)
        if len(temp) > len(res):
            res=temp
        
        temp = helper(s, i, i+1)
        if len(temp) > len(res):
            res=temp
    
def helper(string , left, right):
    if left >= 0 and right < len(string) and string[left]==string[right]:
        left -=1
        right +=1
    return string[left+1:right]