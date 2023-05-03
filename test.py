

# Random Graph
G = nx.Graph()

# Add nodes to the graph
for i in range(10):
    G.add_node(i)


for i in range(10):
    for j in range(i+1, 10):
        if random.random() < 0.5:
            G.add_edge(i, j)

# Print the graph
# print(G.edges())


communities = community.greedy_modularity_communities(G)


# Calculate the conductance of all partitions
con = []
for i in enumerate(list(communities)):
    c = community.conductance(G, communities[i])
    #c = nx.algorithms.cuts.conductance(G, communities[i])
    con.append(list(c))


# print(f"Conductance {i+1}: {conductances[i]}")
# Print the conductance of each partition
# for i, conductance in enumerate(conductances):
# print(f"Conductance= {i+1}: {conductance}")