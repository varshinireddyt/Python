class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    # def __init__(self, vertex):
    #     self.V = vertex
    #     self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def findRoot(self,root,i):
        if root[i] == i:
            return i
        return self.findRoot(root,root[i])

    def unionSum(self,root, visited, x, y):
        xroot = self.findRoot(root,x)
        yroot = self.findRoot(root,y)
        if visited[xroot] > visited[yroot]:
            root[yroot] = xroot
        elif visited[xroot] < visited[yroot]:
            root[xroot] = yroot
        else:
            root[yroot] = xroot
            visited[xroot] += 1


    def mstKruskal(self):
        result = []
        e = 0 #edges
        i = 0#sorted
        self.graph = sorted(self.graph, key=lambda arr: arr[2])
        visited = []
        root = []
        #total = 0

        for node in range(self.V):
            root.append(node)
            visited.append(0)
        # for h in range(self.V):
        #     root.append(h)
        #     visited.append(0)
        print(root)

        while e < self.V-1 :
            u, v, w = self.graph[i]
            i += 1
            x = self.findRoot(root,u)
           # print(x)
            y = self.findRoot(root, v)
           # print(y)
            if  x != y:
                e += 1
                #total += w
                result.append([u,v,w])
                self.unionSum(root, visited, x, y)
    #    for u,v, w in result:
       #     print( u,v,w)
            #print(total)
        return result



g = Graph(6)
g.addEdge(1,2,3)
g.addEdge(1,4,1)
g.addEdge(4,5,2)
g.addEdge(1,5,5)
g.addEdge(2,3,2)
g.addEdge(4,3,3)
# g.add_edge(0, 1, 4)
# g.add_edge(0, 2, 4)
# g.add_edge(1, 2, 2)
# g.add_edge(1, 0, 4)
# g.add_edge(2, 0, 4)
# g.add_edge(2, 1, 2)
# g.add_edge(2, 3, 3)
# g.add_edge(2, 5, 2)
# g.add_edge(2, 4, 4)
# g.add_edge(3, 2, 3)
# g.add_edge(3, 4, 3)
# g.add_edge(4, 2, 4)
# g.add_edge(4, 3, 3)
# g.add_edge(5, 2, 2)
# g.add_edge(5, 4, 3)
g.mstKruskal()
#print(g.mstKruskal())






