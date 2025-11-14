"""
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

list1 = [1,2,4]
list2 = [1,3,4]

list3 = list1 + list2
list3.sort()
print(list3)