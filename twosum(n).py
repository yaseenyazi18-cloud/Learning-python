
"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twosum(nums,target):
    prev_map = dict()
    for i,num in enumerate(nums):
        if target - num in prev_map:
            return [i,prev_map[target-num]]
        prev_map[num] = i
    return-1    

nums = [2,7,11,15]
target = 9          
result = twosum(nums,target)  
print(result) 