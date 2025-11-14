"""
Input: prices = [7,1,5,3,6,4]
Output: 5

"""
prices = [7,1,5,3,6,4]

left, right = 0, 1
profit = 0

while right < len(prices):
    if prices[left] < prices[right]:
        profit = max(profit, prices[right] - prices[left])
    else:
        left = right 
    
    right += 1
           
print(profit)