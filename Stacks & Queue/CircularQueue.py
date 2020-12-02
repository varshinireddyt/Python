class Queue:
    def __init__(self,size):
        self.q = list()
        self.front = -1
        self.rear = -1
        self.maxSize = size

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def size(self):
        if self.rear >= self.front:
            return self.rear-self.front
        return self.maxSize - (self.front - self.rear)

    def isFull(self):
        if self.size == self.maxSize:
            return True
        return False

    def push(self,element):
        if self.isEmpty() == True:
            self.front = 0
            self.rear = 0
            self.q[self.rear] = element

        elif self.isFull() == True:
            return 'Queue is Full'

        else:
            self.rear = (self.rear + 1) % self.maxSize
            self.q[self.rear] = element

    def pop(self):
        if self.isEmpty() == True:
            return 'Queue is Empty'
        elif self.front == self.rear:
            self.front -= 1
            self.rear -= 1
        else:
            self.front = (self.front + 1) % self.maxSize



