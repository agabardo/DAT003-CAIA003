import graphviz

# Leia o conteúdo do arquivo DOT colorido
with open('karate.dot', 'r') as file:
    dot_source = file.read()

# Crie um gráfico Graphviz a partir do conteúdo DOT
g = graphviz.Source(dot_source)

# Renderize e exiba o gráfico
g.view()
