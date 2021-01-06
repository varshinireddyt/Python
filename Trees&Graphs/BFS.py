
from queue import Queue
class BreadthFirstSearch:
    def bfs(self,graph,node, visited=[]):
        visited.append(node)
        q = Queue()
        q.put(node)
        while not q.empty():
            x = q.get()
            for vertex in graph[x]:
                if vertex not in visited:
                    visited.append(vertex)
                    q.put(vertex)
        return visited

if __name__ == '__main__':
    obj = BreadthFirstSearch()
    graph = {1: [2, 3, 5], 2: [1, 4], 3: [1, 5], 4: [2], 5: [1, 3]}
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
    #visited = [0] * len(graph)
    print(obj.bfs(graph,'A'))
