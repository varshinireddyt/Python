
"""
Leetcode: Best time to buy and sell stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
def maxProfit(prices):
    if len(prices) == 0 or len(prices) == 1:
        return 0
    profit = prices[1]-prices[0]
    min_value = prices[0]
    for i in range(1,len(prices)):
        temp = prices[i] - min_value
        if temp > profit:
            profit = temp
        if prices[i] < min_value:
            min_value = prices[i]
    return 0 if profit < 0 else profit


#prices = [7,6,4,3,2,1]
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
