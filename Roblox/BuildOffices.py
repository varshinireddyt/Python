import itertools
from collections import deque
def findMinDistance(w, h, n):
    arr = []
    res = float('inf')
    for i in range(h):
        for j in range(w):
            arr.append((i,j,0))
    for points in itertools.combinations(arr,n):
        q = deque([])
        visited = set()
        for x,y, dist in points:
            q.append((x,y,dist))
            visited.add((x,y))
        ansDist = 0
        arrDist = []
        while q:
            i, j, dist = q.popleft()
            ansDist = max(dist, ansDist)
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<h and 0<=y<w and (x,y) not in visited:
                    q.append((x,y,dist+1))
                    visited.add((x,y))
        res = min(ansDist,res)
    return res