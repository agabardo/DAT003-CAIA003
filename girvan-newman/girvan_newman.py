import networkx as nx
# Crie o grafo do Karate
G = nx.karate_club_graph()
modularity = nx.community.modularity(G, nx.community.label_propagation_communities(G))

print(modularity)

nx.write_graphml(G, 'karate_club_label_propagation.graphml')
