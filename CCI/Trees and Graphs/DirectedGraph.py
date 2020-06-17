"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Performing BFS using queue to find the route between two nodes.S
"""
from collections import  deque
class Graph:
    def __init__(self, edges, N):
        self.adjacent = [[] for i in range(N)]
        for (source,dest) in edges:
             self.adjacent[source].append(dest)

def isConnected(graph,source,dest, visited):
    q  = deque()
    visited[source] = True    #source vertex is visited
    q.append(source)
    while q:
        v = q.popleft()
        if v == dest:    #if destination found
            return True
        for u in graph.adjacent[v]:    #for every adjacent node(v -> u)
            if not visited[u]:
                visited[u] = True       #marking as visited
                q.append(u)             #append to the queue
    return False
if __name__ == '__main__':
    edges = [(0,3),(1,0),(1,2),(1,4),(2,7),(3,4),(3,5),(4,3),(4,6),(5,6),(6,7) ]   #edges of the graph
    N = 8   #number of nodes in the graph
    graph = Graph(edges,N)
    visited =  [False] * N
    (source, dest) = (0,1)   #sourcea and destination vertex
    if isConnected(graph,source,dest,visited):
        print("Route exists between ", source, " to ", dest)
    else:
        print("No Route exists between ", source, " to ", dest)





