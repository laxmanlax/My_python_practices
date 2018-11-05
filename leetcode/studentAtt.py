def checkRecord(s):
    """
    You are given a string representing an attendance record for a student. The record only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
    A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
    
    You need to return whether the student could be rewarded according to his attendance record.
    
    Example 1:
    Input: "PPALLP"
    Output: True
    Example 2:
    Input: "PPALLL"
    Output: False
    
        :type s: str
        :rtype: bool
    """
    status = False
    stud = ""
    count = 1

    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            if s[i-1] == "A" and count == 1 or s[i-1] == "L" and count <= 2:
                status = True
            else:
                status = False
            count = 1

    if s[i] in ["A", "L"]:
        if s[i] == "A" and count == 1 or s[i] == "L" and count <= 2:
            status = True
        else:
            status = False
    else:
        pass

    return status


s = "PPALLP"
s = "PPALLL"
print (checkRecord(s))
