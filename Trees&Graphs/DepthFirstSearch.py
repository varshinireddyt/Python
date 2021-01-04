"""
Depth First Search
Time complexity: O(V + E), V - vertices, E - edges
"""
from queue import LifoQueue

class DepthFirstSearch():

    def dfsUsingRecursion(self, graph, vertex, visited = []):
        if vertex not in visited:
            visited.append(vertex)
            for i in graph:
                self.dfsUsingRecursion(graph, i, visited)
        return visited


    def dfsUsingStack(self, graph, vertex):
        stack = LifoQueue()
        stack.put(vertex)
        visited = []
        while not stack.empty():
            node = stack.get()
            #print(node)
            if node not in visited:
                visited.append(node)
            for i in graph[node]:
                #print('i: ',i)
                if i not in visited:
                    stack.put(i)

        return visited



if __name__ == '__main__':
    obj = DepthFirstSearch()
    #graph = {1:[2,3,5],2:[1,4],3:[1,5],4:[2],5:[1,3]}
    #visited = [0] * len(graph)  # length of graph is number of vertices
    graph = {
        'A': ['B', 'S'],
        'B': ['A'],
        'C': ['D', 'E', 'F', 'S'],
        'D': ['C'],
        'E': ['C', 'H'],
        'F': ['C', 'G'],
        'G': ['F', 'S'],
        'H': ['E', 'G'],
        'S': ['A', 'C', 'G']
    }

    print(obj.dfsUsingRecursion(graph,'A'))
    print(obj.dfsUsingStack(graph,'A'))


