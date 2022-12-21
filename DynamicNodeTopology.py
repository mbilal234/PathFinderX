# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:18:31 2022

@author: Muhammad Bilal
"""

import networkx as nx
import random
import math

# Create an empty graph
G = nx.Graph()

# Add the source vertex and destination vertex
G.add_node(1)
G.add_node(100)

# Add the intermediate vertices
for i in range(2, 100):
    G.add_node(i)

# Add edges from the source vertex to the intermediate vertices
G.add_edge(1, 2, distance=random.uniform(1, 10), speed=random.uniform(6, 9))
G.add_edge(1, 3, distance=random.uniform(1, 10), speed=random.uniform(6, 9))
G.add_edge(1, 4, distance=random.uniform(1, 10), speed=random.uniform(6, 9))

# Add edges from the intermediate vertices to the destination vertex
G.add_edge(97, 100, distance=random.uniform(1, 10), speed=random.uniform(6, 9))
G.add_edge(98, 100, distance=random.uniform(1, 10), speed=random.uniform(6, 9))
G.add_edge(99, 100, distance=random.uniform(1, 10), speed=random.uniform(6, 9))

# Add edges between the intermediate vertices
for i in range(2, 100):
    for j in range(1, 5):
        G.add_edge(i, i+j, distance=random.uniform(1, 10), speed=random.uniform(6, 9))

source = 1
destination = 103

# Calculate the total number of paths from the source to the destination
shortest_path = nx.shortest_path(G, source, destination)
print(f"The shortest path is: {shortest_path}")

# Select the optimal path
min_delay = 0
optimal_path = None

num_hops = nx.shortest_path_length(G, source, destination)
print(f'Number of hops: {num_hops}')

min_delay = 0
for i in range(num_hops):
    try:
        # Get the edge data for the current edge
        edge_data = G.get_edge_data(shortest_path[i+1], shortest_path[i+2])
        # Calculate the delay for the current edge using the distance and speed attributes
        delay = (edge_data['distance'] / edge_data['speed']) * 1000
        min_delay += delay
    except:
        pass
print(f"The delay from source to destination is: {min_delay:.2f} ms")

#Copy code
