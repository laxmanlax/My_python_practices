## input  = [1,2,3,4,5]
## output = [120, 60, 40, 30, 24]

"""
#Solution 1
def productall(input):
    result  = []
    for i in range(len(input)):
        temp =  input[0:i] + input[i+1:]
        allproduct = reduce(lambda x,y:x*y ,temp)
        result.append(allproduct)

    print result

input = [1,2,3,4,5]
productall(input)

"""


[1, 2, 6, 24]
[5, 20, 60, 120]

[120, 60, 40, 30, 24]
