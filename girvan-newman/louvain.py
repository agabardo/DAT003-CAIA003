import community as community_louvain
import networkx as nx

def louvain_communities(G):
    # Executa o algoritmo de Louvain para detecção de comunidades
    partition = community_louvain.best_partition(G)
    
    # Organiza os nós por comunidades
    communities = {}
    for node, community in partition.items():
        communities.setdefault(community, []).append(node)
    
    return communities

def gerar_dot_colorido(G, communities):
    dot_content = "graph G {\n"
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']  # Adicione mais cores se necessário

    for community_id, nodes in communities.items():
        for node in nodes:
            dot_content += f'    {node} [style=filled, color={colors[community_id % len(colors)]}];\n'
    
    for edge in G.edges:
        dot_content += f'    {edge[0]} -- {edge[1]};\n'
    
    dot_content += "}\n"
    return dot_content

# Crie o grafo do Karate
G = nx.karate_club_graph()
communities = louvain_communities(G)

# Imprima os resultados
for community_id, nodes in communities.items():
    print(f"Comunidade {community_id}: {nodes}")

# Gere o conteúdo do arquivo DOT com cores
dot_source = gerar_dot_colorido(G, communities)

# Salve o arquivo DOT
with open('louvain_colored.dot', 'w') as file:
    file.write(dot_source)

nx.write_graphml(G, 'karate_club_louvain.graphml')

