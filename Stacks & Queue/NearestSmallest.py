from queue import Queue
from queue import LifoQueue
def nearestSmallest(arr):
    q = Queue()
    res = []
    for i in range(len(arr)):
        q.put(arr[i])
    while q.empty() != True:
        if len(res) == 0:
            res.append(-1)
            prev = q.get()
        else:
            curr = q.get()
            if prev < curr:
                res.append(prev)
                prev = curr
            else:
                i = 0
                while i <= len(res):
                    if res[len(res)-i-1] > curr :
                        i += 1
                    else:
                        res.append(res[len(res)-i-1])
                        prev = curr
                        break
    return res

def leftSmallest(arr):
    res = []
    stack = LifoQueue()
    for i in range(len(arr)):
        while stack.empty() != True:
            prev = stack.get()
            if prev < arr[i]:
                res.append(prev)
                stack.put(prev)
                break
        if stack.empty() == True:
            res.append(-1)
        stack.put(arr[i])
    return res



arr = [2,4,10,5,1]
#arr = [1,6,4,10,2,5]
#print(nearestSmallest(arr))
print(leftSmallest(arr))











