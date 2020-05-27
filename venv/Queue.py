class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return  self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue

nums = Queue()
nums.enqueue(10)
nums.enqueue(20)
nums.enqueue(30)
nums.dequeue()
print(nums.printQueue())