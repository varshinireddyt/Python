def optimizeBox(arr,n):
    boxDict = {}
    for num in arr:
        if num in boxDict:
            boxDict[num] += 1
        else:
            boxDict[num] = 1
    numArr = [(key,val) for key,val in boxDict.items()]

    numArr.sort(key = lambda x : (-x[0],-x[0]*x[1]))
    maxWeight = sum(arr)
    A = []
    currWeight = 0
    for i , j in numArr:
        if currWeight + (i * j) < maxWeight - currWeight:
            currWeight += (i * j)
            A += ([i] * j)
    if currWeight > maxWeight-currWeight:
        return A
    else:
        return [x for x in arr if x not in A]


arr = [5,3,2,4,1,2]
n = 6
arr = [2,1,1,1]
n = 4
print(optimizeBox(arr,n))

