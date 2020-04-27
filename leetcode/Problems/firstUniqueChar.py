"""
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

def firstUniqChar(s):
    cnt = dict()
    
    for i in s:
        if i not in cnt:
            cnt[i]=1
        else:
            cnt[i]=cnt[i] + 1
                    
    print cnt 

    for i in range(len(s)):
        if cnt[s[i]]==1:
            return i 
    
    return -1 
    

s = "loveleetcode"
print firstUniqChar(s)    