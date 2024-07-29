import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add edges
G.add_edge(1, 2, capacity=1)
G.add_edge(1, 3, capacity=4)
G.add_edge(2, 3, capacity=3)
G.add_edge(2, 4, capacity=3)
G.add_edge(3, 4, capacity=2)

# Solve the model
flow_value, flow_dict = nx.maximum_flow(G, 1, 4)

print('Maximum Flow: ', flow_value)
print('')

for key_i, inner_dict in flow_dict.items():
    for key_j, inner_value in inner_dict.items():
        print(f"{key_i} --> {key_j}\tFlow: {inner_value}")