def SelectionSort(A, n):
    for i in range(n):
        for j in range(n-1):
            if  A[j] > A[i]:

                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    
    return  A     
A = [2,7,4,1,5,3]
print SelectionSort(A, len(A))