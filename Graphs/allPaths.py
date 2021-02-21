# Python program to print all paths from a source to destination.

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'. 
	visited[] keeps track of vertices in current path. 
	path[] stores actual vertices and path_index is current 
	index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path, allPaths):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            allPaths.append(path)
            print(allPaths)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path, allPaths)

        # Remove current vertex from path[] and mark it as unvisited
        a = path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'

    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False]*(self.V)

        # Create an array to store paths
        path = []
        allPaths = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path, allPaths)
        print(allPaths)


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(0, 4)
g.addEdge(0, 3)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)

s = 0
d = 4
print("Following are all different paths from % d to % d :" % (s, d))
g.printAllPaths(s, d)
# This code is contributed by Neelam Yadav
