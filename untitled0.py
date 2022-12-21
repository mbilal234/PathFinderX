
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

# Assign random values between 1 and 15 to each link


# For each node, connect it to 5 other nodes using the 3 interfaces available
neighbors = list(G.nodes())
print(neighbors)
for i in range(num_nodes):
 
    nextList = random.sample(neighbors, 5)
   
    """   for i in nextList:
        if i in neighbors:
            neighbors.remove(i)      """  
    for j in neighbors:
        G.add_edge(i, j,weight = random.randint(1,15))


# Select the source and destination nodes, ensuring that the source is at least 70 nodes away from the destination
source = 0
while True:
    destination = random.randint(0, num_nodes - 1)
    if source != destination and nx.shortest_path_length(G,source,destination)>70:
        break
# Calculate the total number of paths from the source to the destination
shortest_path = nx.shortest_path(G,source,destination)
print(f"The shortest path is: {shortest_path}")
paths = nx.all_simple_paths(G, source, destination)
print(f'Total number of paths: {len(list(paths))}')

# Select the optimal path by considering delay as a metric
min_delay = float('inf')
optimal_path = None
for path in paths:
    delay = 0
    for i in range(len(path) - 1):
        delay += G[path[i]][path[i + 1]]['weight']
    if delay < min_delay:
        min_delay = delay
        optimal_path = path
print(f'Optimal path: {optimal_path}')

# Calculate the number of hops for the optimal path
num_hops = nx.shortest_path_length(G, source, destination)
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
