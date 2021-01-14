import heapq

def maximumUnits(boxTypes,truckSize):
    heap = []
    for box,units in boxTypes:
        heapq.heappush(heap, [-units,box])

    totalUnits = 0
    while heap and truckSize > 0:
        x = heapq.heappop(heap)
        boxNum = min(truckSize, x[1])
        totalUnits += boxNum * (x[0] * (-1))
        truckSize -= boxNum
    return totalUnits


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(maximumUnits(boxTypes,truckSize ))