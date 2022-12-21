# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:52:43 2022

@author: Muhammad Bilal
"""

import networkx as nx
import random

# Create an empty graph
G = nx.Graph()

# Add the source vertex and destination vertex
G.add_node(1)
G.add_node(100)

# Add the intermediate vertices
for i in range(2, 100):
    G.add_node(i)

# Add edges from the source vertex to the intermediate vertices
G.add_edge(1, 2, weight=random.randint(1, 15))
G.add_edge(1, 3, weight=random.randint(1, 15))
G.add_edge(1, 4, weight=random.randint(1, 15))

# Add edges from the intermediate vertices to the destination vertex
G.add_edge(97, 100, weight=random.randint(1, 15))
G.add_edge(98, 100, weight=random.randint(1, 15))
G.add_edge(99, 100, weight=random.randint(1, 15))

# Add edges between the intermediate vertices
for i in range(2, 100):
    for j in range(1, 5):
        G.add_edge(i, i+j, weight=random.randint(1, 15))

source = 1
destination = 103

# Calculate the total number of paths from the source to the destination
shortest_path = nx.shortest_path(G,source,destination)
print(f"The shortest path is: {shortest_path}")
#paths = nx.all_simple_paths(G, source, destination)
#print(f'Total number of paths: {len(list(paths))}')

# Select the optimal path by considering delay as a metric
min_delay = float('inf')
optimal_path = None
"""for path in shortest_path:
    delay = 0
    for i in range(len(path) - 1):
        delay += G[path[i]][path[i + 1]]['weight']
    if delay < min_delay:
        min_delay = delay
        optimal_path = path
print(f'Optimal path: {optimal_path}')"""


# Calculate the number of hops for the optimal path
num_hops = nx.single_source_shortest_path_length(G, source)
print(f'Number of hops: {num_hops}')

# Transmit 5 packets of equal size from the source to the destination and calculate the average delay and the overhead of the network
packet_size = 1000
num_packets = 5
total_delay = 0
for i in range(num_packets):
    total_delay += min_delay
overhead = (num_packets * packet_size) / (num_packets * packet_size + total_delay)
average_delay = total_delay / num_packets
print(f'Average delay: {average_delay}')
print(f'Overhead: {overhead}')
