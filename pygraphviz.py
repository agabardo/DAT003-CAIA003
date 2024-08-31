import graphviz

# Read the DOT file content
with open('spotify.dot', 'r') as file:
    dot_source = file.read()

# Create a Graphviz graph from the DOT source content
g = graphviz.Source(dot_source)

# Render and display the graph
g.view()
