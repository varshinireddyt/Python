"""
Bellman Ford: (shirtest path from one node to all)
1.Create an Array of distances with distances of all nodes as infinity
2.Make distance of source node to 0
3.Run a loop for i from 0 to V(number of vertices)
4.Inside a loop run another look for j = 0 to E(number of edges)
5.Inside j loop, if the existinf distance of second vertex is more than distance of source vertex and cost of the
edge, then update it.
   if dist[v] > dist[u] + cost[uv]
        dist[v] = dist[u] + cost[uv]

"""
import math
class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    def bellmanFord(self, src):
        dist = [math.inf] * (self.vertex+1)
        #print(dist)
        dist[src] = 0
        for i in range(self.vertex - 1):
            for u, v, w in self.graph:
                if dist[u] != math.inf and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
        return dist


g = Graph(5)
g.addEdge(1,4,1)
g.addEdge(1,2,3)
g.addEdge(2,3,5)
g.addEdge(3,4,5)
g.addEdge(4,3,5)
g.addEdge(4,5,2)
g.addEdge(5,1,5)

print(g.bellmanFord(1))
