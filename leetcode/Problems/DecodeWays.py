"""
Approach 
----------
"3" -> "C"   num_ways("3") =1

" " -> " "   num_ways(" ") =1

Ex : 
12345  ->>       [1]-2345        or        [12]-345      sicne 1 and 12 < 26 
             a + decode("2345")  or    l  + decode("345") 

So we can write it 
num_ways("12345") = num_ways("2345") + num_ways("345)

now in Ex : 
27345 ->>  [2]-7345           beacouse   [27]-345  27 > 26 we can't decode it so
           b + decode("7345") 

So we can write here 
num_ways("27345") = num_ways("7345") 

num_ways("011") = 0 
"""

def helper_dp(data, k, memo):
    if k == 0:  # string is empty helper_dp("") = 1
        return 1

    s  = len(data) - k 
    if data[s] == "0":  # string is empty helper_dp("011") = 0
        return 0 

    if  memo[k]!=0:
        return memo[k]

    result = helper_dp(data, k-1, memo)
    if k >=2 and int(data[s:s+2]) <=26:
        result += helper_dp(data, k-2, memo)

    memo[k] = result 
    return result

def num_ways_dp(data):
    memo = [0 for i in range(len(data)+1)]
    print memo 
    print  helper_dp(data, len(data), memo),("\n")


if __name__=="__main__":
    for data in ["11111","17245","236234","123421","121323"]:
        num_ways_dp(data)

