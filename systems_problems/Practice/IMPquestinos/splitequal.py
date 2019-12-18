"""
Given an array of numbers(ex [3 2 5]), find if its possible to split it into 2 parts with equal 
sum without reordering (ex [3 2 ] and [5] ) and false if not possible! 
"""

def split_equal(num):
	for i in range(len(num)):
		if sum(num[:i]) == sum(num[1:]):
			return True
	
	return False 


def split_equal(num):
	if sum(num)%2 !=0:
		return False

	part = sum(num)//2 

	res = 0
	count = 0
	for i in num:

		count +=i
		if count == part:
			res +=1

	return res == 2




