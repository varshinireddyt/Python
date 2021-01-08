"""
Given a graph where every edge has weight as either 0 or 1. A source vertex is also given in the graph.
Find the shortest path from source vertex to every other vertex.

"""
from sys import maxsize as INT_MAX
from collections import deque

class Node:
    def __init__(self, data, weight):
        self.data = data
        self.weight = weight

vertices = 9
edges = [0] * vertices
for i in range(vertices):
    edges[i] = []

def addEdge(u,v,wt):
    edges[u].append(Node(v,wt))
    edges[v].append(Node(u,wt))

def zeroOneBFS(startNode):
    dist = [0] * vertices
    for i in range(vertices):
        dist[i] = INT_MAX

    Q = deque()
    dist[startNode] = 0
    Q.append(startNode)

    while Q:
        x = Q[0]
        Q.popleft()

        for i in range(len(edges[x])):
            if dist[edges[x][i].data] > dist[x] + edges[x][i].weight :
                dist[edges[x][i].data] = dist[x] + edges[x][i].weight

                if edges[x][i].weight == 0:
                    Q.appendleft(edges[x][i].data)
                else:
                    Q.append(edges[x][i].data)

    return dist

if __name__ == '__main__':
    addEdge(0, 1, 0)
    addEdge(0, 7, 1)
    addEdge(1, 7, 1)
    addEdge(1, 2, 1)
    addEdge(2, 3, 0)
    addEdge(2, 5, 0)
    addEdge(2, 8, 1)
    addEdge(3, 4, 1)
    addEdge(3, 5, 1)
    addEdge(4, 5, 1)
    addEdge(5, 6, 1)
    addEdge(6, 7, 1)
    addEdge(7, 8, 1)

    startNode = 0
    print(zeroOneBFS(startNode))