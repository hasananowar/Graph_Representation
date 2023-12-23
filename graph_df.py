import numpy as np
from scipy.spatial.distance import pdist, squareform
import pandas as pd

def extract_edges(nodes, distance_threshold):
    pairwise_distances = pdist(nodes)
    distance_matrix = squareform(pairwise_distances)
    edges_indices = np.where(distance_matrix < distance_threshold)
    edges = [(i, j) for i, j in zip(edges_indices[0], edges_indices[1]) if i < j]
    return edges

# Load nodes from a Pandas DataFrame
# Example DataFrame with columns X, Y, Z, Atom_Name, Residue_Name, Residue_ID, Atom_Type, and Timeframe
# Load nodes for all timesteps from a .npy file
filepath = '/home/mhanowar/Downloads/dataframe100frames.csv'  # Replace with the actual file path
df = pd.read_csv(filepath)
# interesting atoms
atom_types = ['o', 'os', 'n', 'hn']
df_nodes = df.query('Atom_Type in @atom_types').reset_index(drop=True)
df_nodes
 

# Number of timesteps
# num_timesteps = df_nodes['Timeframe'].nunique()
num_timesteps = 2
# Distance threshold
distance_threshold = 5

# Create an empty DataFrame to store node information for every edge
columns = ['Edge', 'Node1', 'Node2']
df_node_info = pd.DataFrame(columns=columns)

# Iterate over timesteps
for timestep in range(num_timesteps):
    # Get node coordinates for the current timestep
    nodes = df_nodes[df_nodes['Timeframe'] == timestep][['X', 'Y', 'Z']].values

    # Extract edges based on the distance threshold
    edges = extract_edges(nodes, distance_threshold)

    # Save node information to DataFrame
    for edge_num, edge in enumerate(edges):
        node1 = edge[0]
        node2 = edge[1]
        df_node_info = pd.concat([df_node_info, pd.DataFrame({
            'Edge': [edge_num],
            'Node1': [node1],
            'Node2': [node2],
        })], ignore_index=True)

    print(f'Timestep {timestep}: Number of Edges = {len(edges)}')

# Print the shape of the DataFrame
print("DataFrame Shape:", df_node_info.shape)

# Print the DataFrame
df_node_info
