class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        elif self.front == self.rear:
            return True
        else:
            return False

    def push(self, element):
        if self.isEmpty() == True:
            self.front = 0
            self.rear = 0
            self.queue.append(element)
            self.rear += 1
        else:
            self.queue.append(element)
            self.rear += 1

    def remove(self):
        if self.isEmpty() == True:
            return 'Queue is empty'
        else:
            self.front += 1


    def isFull(self):
        if rear == maxsize:
            return True
        else: return False

    def printQueue(self):
        return self.queue



Q = Queue()
maxsize = 8
Q.push(2)
Q.push(4)
Q.push(10)
Q.push(5)
Q.remove()


print(Q.printQueue())
print(Q.remove())




