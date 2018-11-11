def countPalinSubstr(str1):
    count = 0

    for i in range(len(str1)):
        count += helper(str1, i, i)
        count += helper(str1 ,i ,i+1)

    return count

def helper(string, left, right):
    inter_count = 0
    if left >=0 and right < len(string) and string[left]==string[right]:
        inter_count +=1
        left -=1
        right +=1

    return inter_count


str1 = "carerac"
str1="aab"
print countPalinSubstr(str1)
