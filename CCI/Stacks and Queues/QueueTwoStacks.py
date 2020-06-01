"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""
class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def isEmpty(self):
        return len(self.stack1) + len(self.stack2) == 0             # If both stacks are empty

    def enQueue(self,data):
        self.stack1.append(data)                #Appending element to the stack1

    def deQueue(self):
        if len(self.stack2) == 0:                   # if stack 2 is empty then stack1 elements are added to stack2, then pop operation is done
                while len(self.stack1) != 0:
                    self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def printStack(self):
        return self.stack2 + self.stack1


Q = Queue()
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
Q.deQueue()
Q.deQueue()
Q.enQueue(4)
Q.deQueue()
print(Q.printStack())





