import re
def longestCommonPrefix(strs):
    minv = min(strs, key=len)
    maxT = ""

    for i in range(len(minv)):
        if len(re.findall(minv[0:i], " ".join(strs)))==len(strs):
            maxVal = re.findall(minv[0:i], " ".join(strs))[0]

            if len(maxVal) > len(maxT):
                maxT=maxVal

    if maxT:
        return maxT
    else:
        return " "

val = ["flower", "flow", "flight"]
print longestCommonPrefix(val)
