"""
1.A teacher in a class gives assignment to the students, the teacher is letting students to choose work in a group. Students choose there friends in a group
how many assignments teacher should give(one assignment per one group)?


2. maximum number of friends in a group?

Union Find:
multisource BST
"""
#import collections
class Graph:

    def numberOfConnectedComponent(self, graph):
        #visited = []
        #graph = collections.defaultdict(list)
        # for x, y in edges:
        #     graph[x].append(y)
        #     graph[y].append(x)
        def dfs(vertex,visited):    #dfs
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    dfs(node,visited)

        count = 0
        visited = set()
        for node in graph:
            if node not in visited:
                dfs(node,visited)
                count+=1
        return count



if __name__ == '__main__':
    obj = Graph()
    graph = {
        'a': ['b'],
        'b': ['c'],
        'c': ['d'],
        'd': [],
        'e': ['f'],
        'f': []
    }
    #edges = [[1,2],[2,5],[3,4],[8,0]]
    #n=7
    print(obj.numberOfConnectedComponent(graph))

