"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.


Example:
Given "25525511135"
return ["255.255.11.135", "255.255.111.35"]. 
(Make sure the returned strings are sorted in order)

In isValid, strings :
-------
whose length greater than 3 or equals to 0 is not valid; 
or if the string's length is longer than 1 and the first letter is '0' then it's invalid;
or the string whose integer representation greater than 255 is invalid.
----- 
"""
def restorelpAddresses(s):
    ans = list()
    n = len(s)

    for i in range(7):
        for j in range(i,7):
            for k in range(j,n):

                s1 = s[:i]
                s2 = s[i:j]
                s3 = s[j:k]
                s4 = s[k:]

                print s1, "-", s2, "-", s3, "-", s4

                if isvalid(s1) and isvalid(s2) and isvalid(s3) and isvalid(s4):
                    ans.append(s1+'.'+s2+'.'+s3+'.'+s4)
                    
    return sorted(ans)

def isvalid(s):
    ## In_valid condition 
    ## len(s)> 3 or len(s)==0 or len(n)> 1 and n[0]=='0' or int(n) > 255  
    if 1 <= len(s) <= 3 and ((s[0] == '0' and len(s) == 1) or (s[0] != '0')) and 0 <= int(s) <= 255:
        return True 
    return False 

s = "25525511135"
print restorelpAddresses(s)


