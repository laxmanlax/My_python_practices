def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    length = len(s)
    if length % 2 == 0:
        for i in range(len(s)):
            if s.count(s[0:i])*len(s[0:i]) == length:
                return True
    return False


s = "babbabbabbabbab"
print (repeatedSubstringPattern(s)) 
