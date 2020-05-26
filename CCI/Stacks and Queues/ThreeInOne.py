"""
Implementation of N stacks in a single array
"""
class Stacks:

    def __init__(self, N, capacity):
        self.capacity = capacity    # Size of the array
        self.N = N                  # Number of stacks

        self.stackData = [0] * self.capacity   # Initializing the array of size capacity
        self.topOfStack = [-1]  * self.N       # -1 indicates stacks are empty
        self.extra = 0                         # top indexes of the array are stored in the extra stack
        self.nextAvailable = [i + 1 for i in range(self.capacity)] # Incrementing to the next available stack
        self.nextAvailable[self.capacity-1] = -1                    # Incrementing to the next available top pf the stack index

    def isFull(self):
        return self.extra == -1   # -1 indicates stack is full here

    def isEmpty(self, N):
        return self.topOfStack[N] == -1  # top of the stack is empty

    def push(self, num, N):
        if self.isFull():
            print("Stack Overflow")
            return
        insert  = self.extra
        self.extra = self.nextAvailable[self.extra]
        self.stackData[insert] = num   # Inserting the nums to the stackData
        self.nextAvailable[insert] = self.topOfStack[N] # Updating the nextAvailable with the old top of stack
        self.topOfStack[N] = insert                     # Updating the new top of the stack

    def pop(self,N):
        if self.isEmpty(N):
            return None

        top = self.topOfStack[N]
        self.topOfStack[N] = self.nextAvailable[self.topOfStack[N]]    # Updating new top of the stack
        self.nextAvailable[top] = self.extra
        self.extra = top                               # Moving the old top element to the extra or top indexes of the array

        return  self.stackData[top]
    def isFull(self):
        return self.extra == -1   # -1 indicates stack is full here

    def isEmpty(self, N):
        return self.topOfStack[N] == -1  # top of the stack is empty


    def printStack(self, N):
        topElement = self.topOfStack[N]
        while(topElement != -1):
            print(self.stackData[topElement])
            topElement = self.nextAvailable[topElement]



threeStacks = Stacks(3, 9)
threeStacks.push(9, 2)
threeStacks.push(13,2)
threeStacks.push(10,1)
threeStacks.push(15,1)
threeStacks.push(20,0)
threeStacks.push(4,0)
threeStacks.push(1,1)
threeStacks.push(2,2)
threeStacks.push(3,0)
threeStacks.printStack(2)
threeStacks.pop(2)
threeStacks.printStack(2)



