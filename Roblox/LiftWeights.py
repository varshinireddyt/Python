def liftWeights(weights,C):
    knap = [[0 for x in range(C+1)] for  x in range(len(weights)+1)]
    weights = sorted(weights)
    for i in range(len(weights)+1):
        for j in range(C+1):
            if i == 0 or j == 0:
                knap[i][j] =0
            elif weights[i-1] <= j :
                knap[i][j] = max(weights[i-1]+knap[i-1][j-weights[i-1]], knap[i-1][j])
            else:
                knap[i][j] = knap[i-1][j]

    return knap[len(weights)][C]


weights = [1,3,5]
C = 7

print(liftWeights(weights,C))