

import random
import matplotlib.pyplot as plt
import networkx as nx

# Set the number of nodes and the range for the speed of the nodes
num_nodes = 100
min_speed = 6
max_speed = 9
# Generate the positions of the nodes randomly
positions = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_nodes)]

# Create a graph with 100 nodes
G = nx.Graph()
G.add_nodes_from(range(num_nodes))
plt.show(G)
# Assign random values between 1 and 15 to each link


# For each node, connect it to 5 other nodes using the 3 interfaces available
neighbors = list(G.nodes())
print(neighbors)
for i in range(num_nodes):
    count = 5;
    if (i == 0) or (i == num_nodes-1):
        count = 3
    try:
        nextList = random.sample(neighbors, 5)
    except:
        pass
    while count>0:
        G.add_edge(i, random.randint(1,num_nodes),weight = random.randint(1,15))
        count = count-1


# Select the source and destination nodes, ensuring that the source is at least 70 nodes away from the destination
source = 0
"""while True:
    destination = random.randint(0, num_nodes - 1)
    if source != destination and nx.shortest_path_length(G,source,destination)>7:
        break"""

# Calculate the total number of paths from the source to the destination
shortest_path = nx.single_source_shortest_path(G,source)
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
