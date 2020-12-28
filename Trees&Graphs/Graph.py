class Graph:
    def adjancencyMatrix(self, n, edges ):
        graph = [[0 for i in range(n+1)] for j in range(n+1)]
        # for i in range(n+1):
        #     for j in range(n+1):
        #         graph[i][j] = 0
        #print(graph)
        for i in range(len(edges)):
            graph[edges[i][0]][edges[i][1]] = 1
            graph[edges[i][1]][edges[i][0]] = 1

        return graph

    def adjancencyList(self, n, edges):
        dict = {}

        for i in range(len(edges)):
            if edges[i][0] in dict.keys():
                dict[edges[i][0]].append(edges[i][1])
            else:
                dict[edges[i][0]] = [edges[i][1]]
            if edges[i][1] in dict.keys():

                dict[edges[i][1]].append(edges[i][0])
            else:
                dict[edges[i][1]] = [edges[i][0]]

        return dict






edges = [(2,4),(1,3),(3,2)]
n = 4
obj = Graph()
#print(obj.adjancencyMatrix(n,edges))
print(obj.adjancencyList(n,edges))

