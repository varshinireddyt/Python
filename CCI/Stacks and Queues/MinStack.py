"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the
minimum element? Push, pop and min should all operate in 0(1) time.
"""
class Stack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self,data):
        if len(self.stack) == 0:
            self.minimumStack.append(data)
        else:
            minimum = self.minimumStack[-1]
            if data < minimum:
                self.minimumStack.append[data]
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0 and self.stack.pop() == self.minimumStack[-1]:
            self.minimumStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minimumStack[-1]

    def printStack(self):
        return self.stack


minStack = Stack()
minStack.push(-2)
minStack.push(1)
minStack.push(-1)
minStack.pop()
minStack.getMin()
print(minStack.getMin())
# print(minStack.top())
