import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes with demand attributes
# Source node with negative demand (supply)
G.add_node(1, demand=-4, color='#C5E0B4')
G.add_node(2, demand=-2, color='#C5E0B4')

# ski node with positive demands
G.add_node(3, demand=1, color='#F8CBAD')
G.add_node(4, demand=5, color='#F8CBAD')

# Add edges cost attributes
G.add_edge(1, 2, weight=2, capcity=999999)
G.add_edge(1, 3, weight=-5, capcity=999999)
G.add_edge(4, 1, weight=7, capcity=999999)
G.add_edge(2, 3, weight=-1, capcity=999999)
G.add_edge(2, 4, weight=4, capcity=999999)
G.add_edge(3, 2, weight=6, capcity=999999)
G.add_edge(3, 4, weight=3, capcity=999999)

flowCost, flowDict = nx.network_simplex(G)
print('Minimum cost: ', flowCost)
print('')

for key_i, inner_dict in flowDict.items():
    for key_j, inner_val in inner_dict.items():
        print(f'{key_i} --> {key_j}\t Flow: {inner_val}')