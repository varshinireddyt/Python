"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
"""
class TwoSum:
    def __init__(self):
        self.data = []
        self.is_sorted = False

    def add(self,number):
        self.data.append(number)
        self.is_sorted = False

    def find(self, value):
        if not self.is_sorted:
            self.data.sort()
            self.is_sorted = True
        start = 0
        end = len(self.data) - 1

        while start < end:
            sum = self.data[start] + self.data[end]
            if sum < value:
                start += 1
            elif sum > value:
                end -= 1
            else:
                return True
        return False

number = [[], [1], [3], [5], [4], [7]]
obj = TwoSum()
obj.add(number)
value = 4
param_2 = obj.find(value)
