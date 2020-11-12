"""
Leetcode: https://leetcode.com/discuss/interview-question/890290/
"""
# using  heapq
import heapq
def getNumOfPlayers(num,scores,cutOffRank):
    heap = []
    for i, score in enumerate(scores):
        heapq.heappush(heap,-score)  #convert a score to negative

    numOfPlayers = 0
    while heap and numOfPlayers < cutOffRank:
        score = heap[0]
        while heap and heap[0] == score:
            heapq.heappop(heap)
            numOfPlayers += 1
    return numOfPlayers

cutOffRank = 4
num = 5
scores = [2,2,3,4,5]
print(getNumOfPlayers(num,scores,cutOffRank))
