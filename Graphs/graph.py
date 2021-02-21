from collections import defaultdict


class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node):
        def helper(node, visited):
            visited.add(node)
            for to in self.graph[node]:
                if to not in visited:
                    visited.add(to)
                    print(to, end=' ')
                    helper(to, visited)
        visited = set()
        print(node, end=' ')
        helper(node, visited)

    def bfs(self, node):
        visited = []
        queue = []

        visited.append(node)
        queue.append(node)

        while queue:
            curr_node = queue.pop(0)
            print(curr_node, end=' ')

            for neighbour in self.graph[curr_node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def has_path(self, src, dest):
        def findpath(src, dest, visited):
            if src == dest:
                return True
            visited.add(src)
            for neighbour in self.graph[src]:
                if neighbour not in visited:
                    findpath(neighbour, dest, visited)
            return False
        visited = set()
        return findpath(src, dest, visited)


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)

# g.dfs(1)
# print()
# g.bfs(1)

# print()
print(g.has_path(1, 5))
