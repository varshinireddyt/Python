


def minCost(n,cost):

    for i in range(1,n):
        cost[i][0] += min(cost[i-1][1],cost[i-1][2])
        cost[i][1] += min(cost[i-1][0], cost[i-1][2])
        cost[i][2] += min(cost[i-1][1],cost[i-1][0])

    return min(cost[n-1][0],min(cost[n-1][1],cost[n-1][2]))
cost = [[1,2,3],[1,2,3],[3,3,1]]
n = 3
print(minCost(n,cost))