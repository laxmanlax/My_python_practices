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
"""
def checkRecord(s):
    record  =""
    if len(s)<2:
        record = [s]
    else:

        for i in range(1, len(s)):
            if s[i-1]!=s[i]:
                if s[i-1] not in record:
                    record += s[i-1] + " " + s[i]
                else:
                    record += " "+s[i]
            else:
                if s[i-1] not in record:
                    record += s[i-1] + s[i]
                else:
                    record += s[i]
    
        record = record.split() 
    
 
    if "A" in s and "L" in s:
        late = max(filter(lambda x: "L" in x, record),key=len)
        print "ok"
        if "A" in record and record.count("A")==1 and  ( "L" in record or  "LL" in record  and record.count("LL")<=2 and len(late) <=2):
            return True
        else:
            return False
    else:
        print "ok", record 
        if "A" in record and record.count("A")==1 or  "L" in record or  "LL" in record  and record.count("LL")<=2:
            return True
        else:
            return False         
        
        
s="aaaaaaaaaaabbbbccccccccdddddddddd"
s="PPALLLPPALLLPPALLLPPALLLPPALLLPPALLLPPALLLPPALLLPPALLL"
s = "ALLAPPL"
print checkRecord(s)   
        
        