

class Solution:
    def subtractProductAndSum(self,n):
        product = 1
        sum_ = 0
        for i in str(n):
            product *= int(i)
            sum_ += int(i)
        return product - sum_


