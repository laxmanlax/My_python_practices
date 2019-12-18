"""
Write a function to sort a list of integers that looks like this [5,2,0,3,0,1,6,0] -&gt; [1,2,3,5,6,0,0,0] in the most efficient way
"""
def move_zero(nums):
	zcount = nums.count(0)
	nums = [n for n in nums if n!=0]

	for i in range(zcount):
		nums.append(0)

	return nums

def move_zero(nums):
	i, j , count, n = 0, 0, 0, len(nums)

	while i+count < n:
		if nums[j]:
			nums[i] = nums[j]
			i +=1
		else:
			count +=1

		j +=1

	nums[i:] = count*[0]
	return nums


