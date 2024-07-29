# Import necessary libraries matplotlib, networkx
import networkx as nx
import matplotlib.pyplot as plt

# Setup the directed network with node demands and edge costs
# Create a directed graph
G = nx.DiGraph()

# Add nodes with demand attributes
G.add_node(1, demand=-50, color='#C5E0B4') # Source node with negative demand (supply)
G.add_node(2, demand=-40, color='#C5E0B4') 
G.add_node(3, color='#C5E0B4') # Intermediate node
G.add_node(4, demand=60, color='#F8CBAD')# Sink node with positive demand
G.add_node(5, demand=30, color='#F8CBAD')

# Add edges with capacity and cost attributes
G.add_edge(1, 2, weight=2)
G.add_edge(1, 3, weight=4)
G.add_edge(1, 5, weight=9)
G.add_edge(3, 4, weight=1)
G.add_edge(4, 5, weight=3)
G.add_edge(5, 4, weight=2)

# Define the position for nodes
pos = {1:(1,3),2:(1,1),3:(2,2),4:(3,1),5:(3,3)}

node_colors = list(nx.get_node_attributes(G, 'color').values())

# Draw the graph
nx.draw(G, pos, with_labels=True, font_color='red', node_size=2000, node_color=node_colors, font_size=16, font_weight='bold', edge_color='grey', linewidths=2, arrows=True, connectionstyle='arc3, rad =0.1')

edge_labels = dict([((u,v,), f'{d["weight"]}\n\n{G.edges[(u,v)]["weight"]}')

for u, v, d in G.edges(data=True) if pos[u][0] > pos[v][0]])

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title('Network Flow Graph with Infeasible Solution')
plt.show()