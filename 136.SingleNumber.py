"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [2,2,1]
Output: 1
"""

from collections import Counter
nums = [2,2,1,3,3]

result = 0
for n in nums:
    result = result ^ n

print(result)

count = Counter(nums)

for n, c in count.items():
    if c == 1:
       print(n)