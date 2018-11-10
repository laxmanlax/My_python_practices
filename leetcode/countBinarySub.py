def countBinarySubstrings(s):
    prevRunLenght = 0
    curRunLenght = 1
    res = 0

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curRunLenght +=1
        else:
            prevRunLenght = curRunLenght
            curRunLenght = 1

        if prevRunLenght >= curRunLenght:
            res +=1

        print "curRunLenght={} prevRunLenght={} res={} ------- {}{}".format(curRunLenght, prevRunLenght, res, s[i-1],s[i])
    return res

vstring = "00110011"
#vstring = "10101000"
print countBinarySubstrings(vstring) 

