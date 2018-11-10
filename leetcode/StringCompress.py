"""
Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 
Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:
Nothing is replaced.
 
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
"""

def CompressStr(s):
    fstring = ""
    count = 1

    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            count +=1
        else:
            fstring += str(count)+ s[i-1]
            count = 1
    
    fstring += str(count) + s[i]

    return list(fstring)

s="aaabbbcccd"
#s = ["a", "a", "b", "b", "c", "c", "c"]
print CompressStr(s)



    
