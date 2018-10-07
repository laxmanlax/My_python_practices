def countSubstr(s):
    count = 0 

    for i in range(len(s)):
        count += helper(s, i, i)
        count += helper(s, i, i+1)
    return count

def helper(string, left, right):
    inter_count  = 0

    while left >= 0 and right < len(string) and string[left]==string[right]:
        left -=1
        right +=1
        inter_count +=1
    
    return inter_count 

