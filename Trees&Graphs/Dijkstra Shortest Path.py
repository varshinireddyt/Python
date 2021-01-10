
import sys
import heapq
class Graph:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
V = 5
#E = 14
edges = {}  # dict of int to list of tuple
for i in range(V+1):
    edges[i] = []

def addEdges(u,v,w):
    edges[u].append((v,w))
    edges[v].append((u,w))    #[[[2,3],[4,1],[5,5]],


def dijkstra(source,V):
    dist = [ 1500 for i in range(V+1)]
    dist[source] = 0
    heap = []
    heapq.heappush(heap,(0,source))
    visited = [0] * (V+1)
    while heap:
        x = heapq.heappop(heap)
        if visited[x[1]] == 1:
            continue
        visited[x[1]] = 1
        for i in range(len(edges[x[1]])):
            if dist[edges[x[1]][i][0]] > dist[x[1]] + edges[x[1]][i][1]:
                dist[edges[x[1]][i][0]] = dist[x[1]] + edges[x[1]][i][1]
                heapq.heappush(heap,(edges[x[1]][i][1], edges[x[1]][i][0]))
    return dist


if __name__ == '__main__':
    addEdges(1, 2, 3)
    addEdges(1, 4, 1)
    addEdges(1, 5, 5)
    addEdges(4, 3, 3)
    addEdges(4, 5, 2)
    addEdges(4, 3, 3)
    addEdges(2, 3, 5)

    print(dijkstra(1,5))





