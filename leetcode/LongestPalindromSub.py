def longestPalinDrom(s):
    res = ""
    temp =""
    for i in range(len(s)):
        temp = helper(s, i, i)
        if len(temp) > len(res):
            res=temp
        
        temp = helper(s, i, i+1)
        if len(temp) > len(res):
            res=temp
    
    return res 
    
def helper(string , left, right):
    print string, left, right

    while  left >= 0 and right < len(string) and string[left]==string[right]:
        print string[left],string[right]
        left -=1
        right +=1
    print "return",string[left:right]
    return string[left+1:right]

s="aabaabaaa"
s="baa"
print longestPalinDrom(s)
