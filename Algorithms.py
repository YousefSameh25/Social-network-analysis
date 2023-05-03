import community as com
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import networkx as nx
from tkinter import messagebox
import community.community_louvain as cl
from networkx.algorithms import community
from cdlib import evaluation, algorithms
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#===========================================================================================
def Louvain_algorithm(G):

    communities = community.louvain_communities(G)
    # Create a color map for the communities
    colors = {}
    for i, com in enumerate(communities):
        for node in com:
            colors[node] = i * 10

    # Get a list of colors for each node
    node_colors = [colors[n] for n in G.nodes]

    # Draw the network with nodes colored by community
    pos = nx.spring_layout(G)

    nx.draw(G, pos , node_color = node_colors)
    plt.show()
#===========================================================================================
def adjust_graph(G):

    # get the degrees of the nodes
    degrees = dict(G.degree())

    # define a scaling function
    def size_by_degree(degree , max_degree):
        return degree * 200 / max_degree

    # get the maximum degree
    mx = max(dict(G.degree()).values())

    # set the node sizes based on their degree
    node_sizes = [size_by_degree(degrees[node] , mx) for node in G.nodes()]

    # get the spring layout
    pos = nx.spring_layout(G)

    # draw the graph with the new node sizes
    nx.draw(G, node_size = node_sizes , pos = pos , with_labels = True)

    # get the weights of the edges
    weights = dict(nx.get_edge_attributes(G, 'weight'))

    # define a scaling function
    def size_by_weight(weight , max_weight):
        return weight * 2 / max_weight

    # find the maximum weight
    mx2 = max(nx.get_edge_attributes(G, 'weight').values())

    # set the edge sizes based on their weight
    edge_sizes = [size_by_weight(weights[(u, v)] , mx2) for u, v in G.edges()]

    # draw the graph with the new edge sizes
    nx.draw(G, width = edge_sizes , pos = pos , with_labels = True)

    # show the plot
    plt.show()
#===========================================================================================
def Page_Rank(G):
    # Calculate the PageRank scores
    pr = nx.pagerank(G)
    print(pr)
    # Define the node sizes and colors based on the PageRank scores
    node_sizes = [7000 * pr[node] for node in G.nodes()]
    node_colors = [pr[node] for node in G.nodes()]

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.Blues)
    nx.draw_networkx_edges(G, pos)
    plt.show()
#===========================================================================================
def Degree_Centrality(G):

    # Calculate degree centrality
    dc = nx.degree_centrality(G)
    print(dc)

    # Create the Tkinter window
    root = tk.Tk()
    root.title("Degree Centrality")

    # Create the search box and button
    search_frame = ttk.Frame(root)
    search_frame.pack(pady=10)
    search_label = ttk.Label(search_frame, text="Filter by degree centrality ")
    search_label.pack(side=tk.LEFT, padx=5)
    search_entry = ttk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)
    search_button = ttk.Button(search_frame, text="Filter")
    search_button.pack(side=tk.LEFT, padx=5)

    # Create the table
    tree = ttk.Treeview(root, columns=("Node", "Degree Centrality"))
    tree.heading("Node", text="Node")
    tree.heading("Degree Centrality", text="Degree Centrality")

    # Add the data to the table
    for node, degree in dc.items():
        tree.insert("", "end", text="", values=(node, round(degree, 15)))

    # Add the table to the window
    tree.pack(expand=True, fill=tk.BOTH)

    def filter_nodes():
        # Clear the previous selection
        tree.delete(*tree.get_children())

        # Get the filter threshold
        num = float(search_entry.get())

        # Filter the nodes based on the threshold
        for node, degree in dc.items():
            if degree >= num:
                tree.insert("", "end", text="", values=(node, round(degree, 15)))

        H = G.subgraph([n for n in G.nodes() if dc[n] >= num])

        plt.clf()
        pos = nx.spring_layout(H)
        nx.draw_networkx(H, pos=pos)
        plt.show()

    # Bind the search button to the filter_nodes function
    search_button.config(command=filter_nodes)

    # Start the Tkinter event loop
    root.mainloop()
#===========================================================================================
def Closeness_Centrality(G):

    # Calculate degree centrality
    cc = nx.closeness_centrality(G)
    print(cc)
    # Create the Tkinter window
    root = tk.Tk()
    root.title("Closeness Centrality")

    # Create the search box and button
    search_frame = ttk.Frame(root)
    search_frame.pack(pady=10)
    search_label = ttk.Label(search_frame, text="Filter by Closeness centrality ")
    search_label.pack(side=tk.LEFT, padx=5)
    search_entry = ttk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)
    search_button = ttk.Button(search_frame, text="Filter")
    search_button.pack(side=tk.LEFT, padx=5)

    # Create the table
    tree = ttk.Treeview(root, columns=("Node", "Closeness Centrality"))
    tree.heading("Node", text="Node")
    tree.heading("Closeness Centrality", text="Closeness Centrality")

    # Add the data to the table
    for node, degree in cc.items():
        tree.insert("", "end", text="", values=(node, round(degree, 15)))

    # Add the table to the window
    tree.pack(expand=True, fill=tk.BOTH)

    def filter_nodes():
        # Clear the previous selection
        tree.delete(*tree.get_children())

        # Get the filter threshold
        num = float(search_entry.get())

        # Filter the nodes based on the threshold
        for node, degree in cc.items():
            if degree >= num:
                tree.insert("", "end", text="", values=(node, round(degree, 15)))

        H = G.subgraph([n for n in G.nodes() if cc[n] >= num])

        plt.clf()
        pos = nx.spring_layout(H)
        nx.draw_networkx(H, pos=pos)
        plt.show()

    # Bind the search button to the filter_nodes function
    search_button.config(command=filter_nodes)

    # Start the Tkinter event loop
    root.mainloop()
#===========================================================================================
def Betweenness_Centrality(G):

    # Calculate degree centrality
    bc = nx.betweenness_centrality(G)
    print(bc)

    # Create the Tkinter window
    root = tk.Tk()
    root.title("Betweenness Centrality")

    # Create the search box and button
    search_frame = ttk.Frame(root)
    search_frame.pack(pady=10)
    search_label = ttk.Label(search_frame, text="Filter by Betweenness centrality ")
    search_label.pack(side=tk.LEFT, padx=5)
    search_entry = ttk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)
    search_button = ttk.Button(search_frame, text="Filter")
    search_button.pack(side=tk.LEFT, padx=5)

    # Create the table
    tree = ttk.Treeview(root, columns=("Node", "Betweenness Centrality"))
    tree.heading("Node", text="Node")
    tree.heading("Betweenness Centrality", text="Betweenness Centrality")

    # Add the data to the table
    for node, degree in bc.items():
        tree.insert("", "end", text="", values=(node, round(degree, 15)))

    # Add the table to the window
    tree.pack(expand=True, fill=tk.BOTH)

    def filter_nodes():
        # Clear the previous selection
        tree.delete(*tree.get_children())

        # Get the filter threshold
        num = float(search_entry.get())

        # Filter the nodes based on the threshold
        for node, degree in bc.items():
            if degree >= num:
                tree.insert("", "end", text="", values=(node, round(degree, 15)))

        H = G.subgraph([n for n in G.nodes() if bc[n] >= num])

        plt.clf()
        pos = nx.spring_layout(H)
        nx.draw_networkx(H, pos=pos)
        plt.show()



    # Bind the search button to the filter_nodes function
    search_button.config(command=filter_nodes)

    # Start the Tkinter event loop
    root.mainloop()
#===========================================================================================
def Modularity(G):

    cmap = plt.get_cmap('viridis')

    # Check if the graph is directed or undirected
    if G.is_directed():
        print('The graph is directed.\n')

        communities = community.greedy_modularity_communities(G)

        # Calculate Modularity
        modularity = community.modularity(G, communities, weight='weight')
        print(f"Modularity: {modularity}\n")

        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showinfo("Modularity = ", str(modularity))  # Show the message box

        # Visualization
        communities_dictionary = {x: i for i, s in enumerate(communities) for x in s}
        community_values = [list(communities_dictionary.values())]
        # Create a dictionary of node positions
        pos = nx.spring_layout(G)
        # Draw the graph with nodes colored by community
        nx.draw_networkx_nodes(G, pos, node_size=100, cmap=cmap, node_color=community_values)
        nx.draw_networkx_edges(G, pos, alpha=0.5)
        plt.show()

        root.mainloop()

    else:
        print('The graph is undirected.\n')
        # only with undirected Graph
        # # Calculate modularity using Louvain algorithm
        partition = cl.best_partition(G)
        max_modularity = cl.modularity(partition, G, weight='weight')
        # Print modularity score
        print("Modularity:", max_modularity)

        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showinfo("Modularity = ", str(max_modularity))  # Show the message box

        # Visualization
        # Create a dictionary of node positions
        pos2 = nx.spring_layout(G)
        # Draw the graph with nodes colored by community
        nx.draw_networkx_nodes(G, pos2, node_size=100, cmap=cmap, node_color=list(partition.values()))
        nx.draw_networkx_edges(G, pos2, alpha=0.5)
        plt.show()

        root.mainloop()
#===========================================================================================
def Conductance(G):

    communities = community.greedy_modularity_communities(G)
    print(f"Communities:\n {communities}")

    # Convert from frozenset to list
    communities_list = []
    for i in communities:
        communities_list.append(list(i))


    # Print No.of Clusters
    print(f"\nNumber of Clusters: {len(communities)}\n")

    # Calculate Conductance for each Cluster
    conductances = []
    for com in communities_list:
        conductance_ = nx.algorithms.cuts.conductance(G, com, weight='weight')
        conductances.append(conductance_)


    # Print the conductance of each partition
    for i, conductance in enumerate(conductances):
        print(f"Conductance {i + 1}: {conductance}")

    # Get the Minimum Conductance
    mini_conductance = min(nx.conductance(G, cluster_i, weight='weight')
                           for cluster_i in communities_list)
    print(f"\nMinimum Conductance: {mini_conductance}\n")

    # Print Community with minimum Conductance
    CommunitiesOfminiConductance_list = []
    index = 0
    for i in enumerate(conductances):
        if conductances[index] == min(conductances):
            CommunitiesOfminiConductance_list.append(i[0] + 1)
            # print(i)
        index += 1

    # Print No.of Communities have minimum Conductance
    print(f"Number of Clusters which have minimum Conductance: {len(CommunitiesOfminiConductance_list)}")

    # Print The Community/Communities index of minimum Conductance
    print(f"Community with Minimum Coductance: {CommunitiesOfminiConductance_list}")

    communities_dictionary = {x: i for i, s in enumerate(communities) for x in s}
    community_values = [list(communities_dictionary.values())]

    # Create a dictionary of node positions
    pos = nx.spring_layout(G)
    # Draw the graph with nodes colored by conductance score
    cmap = plt.get_cmap('inferno')
    nx.draw_networkx_nodes(G, pos, node_size=100, cmap=cmap, node_color=community_values)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()
    #----------------------------------------------------------------

    # Create the Tkinter window
    root = tk.Tk()
    root.title("Conductance")

    # Create the table
    tree = ttk.Treeview(root, columns=("Cluster", "Conductance"))
    tree.heading("Cluster", text = "Cluster")
    tree.heading("Conductance", text = "Conductance")

    # Add the data to the table
    for i, conductance in enumerate(conductances):
        tree.insert("", "end", text="", values=(i + 1, conductance))

    # Add the table to the window
    tree.pack(expand=True, fill=tk.BOTH)

    root.mainloop()
#===========================================================================================
def NMI(G):
    leiden_communities = algorithms.leiden(G)

    colors = {}

    # Check if the graph is directed or undirected
    if G.is_directed():
        print('The graph is directed.\n')

        # Detect communities in the graph based on betweenness centrality using Girvan-Newman algorithm
        Girvan_communities = algorithms.girvan_newman(G, level=1)

        # Evaluate the similarity between the two sets of communities
        nmi = evaluation.normalized_mutual_information(Girvan_communities, leiden_communities)

        # Visualization
        # create a dictionary mapping community IDs to colors
        for i, community_ in enumerate(Girvan_communities.communities):
            for node in community_:
                colors[node] = plt.cm.Set1(i)

    else:
        print('The graph is undirected.\n')
        # only with undirected Graph
        louvian_communities = algorithms.louvain(G)

        nmi = evaluation.normalized_mutual_information(louvian_communities, leiden_communities)


        # Visualization
        # create a dictionary mapping community IDs to colors
        for i, community_ in enumerate(louvian_communities.communities):
            for node in community_:
                colors[node] = plt.cm.Set1(i)

    print(f"Normalized Mutual Information: {nmi}")

    # create a list of node colors based on the community assignments
    node_colors = [colors[n] for n in G.nodes()]

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos , node_color=node_colors , with_labels = False)
    plt.show()

    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("NMI = ", str(nmi.score))  # Show the message box

    # Start the GUI loop
    root.mainloop()