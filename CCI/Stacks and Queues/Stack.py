class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def printStack(self):
        return self.stack




nums = Stack()
nums.push(1)
nums.push(2)
nums.push(3)
nums.push(4)
nums.pop()
print(nums.printStack())


# printStack(nums)
