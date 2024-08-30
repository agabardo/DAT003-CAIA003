import numpy as np
import networkx as nx
import random

def kmeans_agrupamento_grafo(G, k, max_iter=100):
    centroides = random.sample(list(G.nodes), k)
    
    for _ in range(max_iter):
        clusters = {i: [] for i in range(k)}
        
        for no in G.nodes:
            distancias = [nx.shortest_path_length(G, source=no, target=centroide) for centroide in centroides]
            centroide_mais_proximo = np.argmin(distancias)
            clusters[centroide_mais_proximo].append(no)
        
        novos_centroides = []
        for i in range(k):
            subgrafo = G.subgraph(clusters[i])
            novo_centroide = min(subgrafo.nodes, key=lambda n: sum(nx.shortest_path_length(subgrafo, source=n).values()))
            novos_centroides.append(novo_centroide)
        
        if novos_centroides == centroides:
            break
        centroides = novos_centroides
    
    return clusters, centroides

def gerar_dot_colorido(G, clusters):
    dot_content = "graph G {\n"
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']  # Add more colors if k > 6

    for cluster_id, nodes in clusters.items():
        for node in nodes:
            dot_content += f'    {node} [style=filled, color={colors[cluster_id % len(colors)]}];\n'
    
    for edge in G.edges:
        dot_content += f'    {edge[0]} -- {edge[1]};\n'
    
    dot_content += "}\n"
    return dot_content

# Crie o grafo e execute o K-means
G = nx.karate_club_graph()
k = 3
clusters, centroides = kmeans_agrupamento_grafo(G, k)

# Gere o conteúdo do arquivo DOT com cores
dot_source = gerar_dot_colorido(G, clusters)

# Salve o arquivo DOT
with open('karate.dot', 'w') as file:
    file.write(dot_source)
