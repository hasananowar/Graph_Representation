import numpy as np
from scipy.spatial.distance import pdist, squareform
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def extract_edges(nodes, distance_threshold):
    pairwise_distances = pdist(nodes)
    distance_matrix = squareform(pairwise_distances)
    edges_indices = np.where(distance_matrix < distance_threshold)
    edges = [(i, j) for i, j in zip(edges_indices[0], edges_indices[1]) if i < j]
    return edges

def display_graph(nodes, edges):
    G = nx.Graph()

    for i, coordinates in enumerate(nodes):
        G.add_node(i, pos=(coordinates[0], coordinates[1]))

    G.add_edges_from(edges)

    node_positions = nx.get_node_attributes(G, 'pos')

    plt.figure(figsize=(16, 16))
    plt.title(f'Graph')
    nx.draw(G, pos=node_positions, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8, edge_color='gray')
    plt.show()


# Load nodes for all timesteps from a .npy file
nodes_file = '/home/mhanowar/Downloads/data10k.npy'  # Replace with the actual file path
all_nodes = np.load(nodes_file)

# Number of timesteps
distance_threshold = 12

# Get node coordinates
nodes = all_nodes[0]

# Extract edges based on the distance threshold
edges = extract_edges(nodes, distance_threshold)

# Display the graph at each timestep
display_graph(nodes, edges)

print (len(edges))

