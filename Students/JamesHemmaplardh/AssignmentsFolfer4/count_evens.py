def count_evens(nums):
"""return the number of even numbers in a given array"""
    x = 0
    for i in nums:
        if i % 2 == 0:
            x += 1
    return x