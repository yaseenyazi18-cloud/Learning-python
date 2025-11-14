"""
Input: nums = [1,2,3,1]
Output: true                   
         
"""
nums = [1,2,3,4,5,6,7,8,8,9]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                         
nums.sort()
print(nums)
i=0
while i < len(nums)-1:
    if nums[i] == nums[i+1]:               
       print(True)                                                             
       break
    else:                
        i = i+1                                          
print(False)                                                                                                                                                                                                                                                                                                                                                 
print("\n---------------0(n)---------------------\n")
num = [2,3,4,5,6,7,2,3,4,3,4,5,5]
hash_set = set()

for i in num:
    if i in hash_set:
        print(True)                    
        break
    hash_set.add(i)  
print(False)        
                             