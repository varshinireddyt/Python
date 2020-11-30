class Queue:

    def __init__(self):
        self.items = []

    def pushFront(self, item):
        self.items.append(item)

    def pushRear(self, item):
        self.items.insert(0, item)

    def popFront(self):
        return self.items.pop()

    def popRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


    def printQueue(self):
        return self.items

    def fetchFront(self):
        if self.isEmpty() == True:
            return 'Queue is empty'
        return self.items[0]

    def fetchRear(self):
        if self.isEmpty() == True:
            return 'Queue is empty'
        return self.items[len(self.items)-1]


Q = Queue()
Q.pushFront(2)
Q.pushFront(4)
Q.pushFront(10)
Q.pushRear(5)


print(Q.printQueue())
print(Q.popFront())

