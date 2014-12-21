"""return the number of even numbers in a given array"""
def count_evens(nums):
	return len([i for i in nums if i % 2 ==0])

