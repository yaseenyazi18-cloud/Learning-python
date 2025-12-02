def searchInsert(nums,target):
    low = 0
    high = len(nums)-1
    found = False
    
    while low <= high:
    
        mid = (low + high) // 2
        
        if nums[mid] == target:
            found = True
            return mid #targetfound at mid intex
        elif nums[mid] < target:
            low = mid + 1 #search in the right half
        else:
            high = mid - 1 # search in the left half   
            
    if found == True:
        print(f"tarjet is founded:")
    else:
        print(f"taeget not founded:")   

nums = [1,3,5,6]
target = 5
nums = [1,3,5,6] 
target = 2
nums = [1,3,5,6] 
target = 7
mid_piont1 = searchInsert(nums, target)
mid_piont2 = searchInsert(nums, target)
mid_piont3 = searchInsert(nums, target)

print(mid_piont1)
print(mid_piont2)
print(mid_piont3)
