"""
Given an integer n, your task is to calculate the alternating sum of its digits. In other words, add up all the digits, alternating between positive and negative.
For example, if n = 52134, the answer should be 5 - 2 + 1 - 3 + 4 = 5.
Example
• For n = 52134, the output should be numberSigningSum(n) = 5.
5 - 2 + 1 - 3 + 4 = 5
• For n = 12345, the output should be numberSigningSum(n) = 3.
1 - 2 + 3 - 4 + 5 = 3
• For n = 104956, the output should be numberSigningSum(n) = -5.
1 - 0 + 4 - 9 + 5 - 6 = -5
Input/Output
• [execution time limit] 3 seconds (java)
• [input] integer n
A positive integer number.
Guaranteed constraints:
1 ≤ n ≤ 109.
• [output] integer
The alternating sum resulting from the digits of n.
"""

def numberSigingSum(n):
    num = [i for i in str(n)]
    sum = 0
    for ind in range(len(num)):
        if ind % 2 == 0:
            sum = sum + int(num[ind])
        else:
            sum= sum - int(num[ind])

    return sum

n = 52134
n = 104956
print(numberSigingSum(n))