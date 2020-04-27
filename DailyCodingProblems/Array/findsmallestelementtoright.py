

def smallestelement(array):
    result = []
    for i in range(len(array)):
        temp = array[i]
        subarry = sorted(array[i:])
        count = 0

        for x in subarry:
            if x < temp :
                count +=1
            else:
                break
        result.append(count)

    return result



array = [3,4,9,6,1]
print smallestelement(array)
