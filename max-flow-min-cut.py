import networkx as nx

# create a directed graph
G = nx.DiGraph()

# add edges
G.add_edge(1, 2, capacity=1)
G.add_edge(1, 3, capacity=4)
G.add_edge(2, 3, capacity=2)
G.add_edge(2, 4, capacity=3)
G.add_edge(3, 4, capacity=2)

# use max-flow min-cut therom
cut_value, partition = nx.minimum_cut(G, 1, 4)

print('capacity of minimum cut: ', cut_value)
print('\n', partition)

reachable, nonreachable = partition

# forward cut
cutset = set()
for u, nbrs in ((n, G[n]) for n in reachable):
    cutset.update((u, v) for v in nbrs if v in nonreachable)
print('forward cut set: ', sorted(cutset))

# reverse cut
reversecutset = set()
for u, nbrs in ((n,G[n]) for n in nonreachable):
    reversecutset.update((u, v) for v in nbrs if v in reachable)
print('reverse cut set: ', sorted(reversecutset))