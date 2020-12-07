from queue import LifoQueue
def numberOfDisks(N,disks):
    buffer = LifoQueue()
    res = []
    i = 0
    prev = 0
    curr = 0
    while i <= N:
        if i == 0:
            buffer.put(disks[i])
            i += 1
            continue
        if i >= N:
            curr = -1
        else:
            curr = disks[i]
        prev = disks[i-1]
        if prev < curr:
            res.append([])
            buffer.put(curr)
        if prev > curr:
            temp = []
            while buffer.empty() == False:
                data = buffer.get()
                print('data: ',data)
                temp.append(data)
            buffer.put(curr)
            res.append(temp)
        i+=1
    return res



N = 5
disks = [4,5,1,2,3]
print(numberOfDisks(N,disks))

# stack = LifoQueue()
# for i in range(len(disks)):
#     stack.put(disks[i])
#
# print(stack)
# while stack








