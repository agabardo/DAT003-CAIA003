from graph_tools import Graph
import graphviz

# create a graph with four nodes and two edges
g = Graph(directed=True)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_vertex(4)
print(g)

# find the all shortest paths from vertex 1
dist, prev = g.dijkstra(1)
print(dist)


g = Graph(directed=False).create_graph('barabasi', 100)
print(g)

# check if all vertices are mutually connected
print(g.is_connected())
