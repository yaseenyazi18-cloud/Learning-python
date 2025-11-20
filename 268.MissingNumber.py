"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1:
Input: nums = [3,0,1]
output: 2
"""
nums = [3,0,1]
res = len(nums)

for i in range(len(nums)):
    res += i - nums[i]

print(res)