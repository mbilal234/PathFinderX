import networkx as nx
import matplotlib as plt
import random
import time
# Generate the random positions of the nodes and create the graph
G = nx.random_geometric_graph(100, 0.125)


# Add the connections between the nodes
for node in G.nodes():
  neighbors = list(G.neighbors(node))
  if len(neighbors) < 5:
    # Connect the node to 5 other random nodes
    while len(neighbors) < 5:
      new_neighbor = random.choice(list(G.nodes()))
      if new_neighbor not in neighbors:
        G.add_edge(node, new_neighbor)
        neighbors.append(new_neighbor)
  else:
    # Disconnect the node from excess neighbors
    while len(neighbors) > 5:
      G.remove_edge(node, neighbors.pop())

# Assign random values to the links
for u, v in G.edges():
  G[u][v]['value'] = random.randint(1, 15)
  

# Find the total number of paths from the source to the destination using DFS
source = 0  # choose the source node
destination = 70  # choose the destination node
total_paths = 0
visited = set()
stack = [(source, [source])]
while stack:
  (vertex, path) = stack.pop()
  if vertex not in visited:
    visited.add(vertex)
    for neighbor in G.neighbors(vertex):
      if neighbor == destination:
        total_paths += 1
      else:
        stack.append((neighbor, path + [neighbor]))

# Find the optimal path using Dijkstra's algorithm
optimal_path = nx.dijkstra_path(G, source, destination, weight='value')

# Calculate the number of hops for the optimal path
num_hops = len(optimal_path) - 1


# Transmit the packets using OSPF routing
packet_size = 1000

# Initialize variables
total_delay = 0
total_data = 0

def transmit_packet(G, packet_size, next_hop):
  # Find the edge connecting the current node and the next hop
  data = G[u][v]
  
  # Simulate an error rate of 10%
  if random.uniform(0, 1) < 0.1:
    # Drop the packet
    return
  
  # Simulate a transmission delay of 0.1 seconds
  time.sleep(0.1)
  
  # Transfer the packet to the next hop
  

# Transmit the packets using OSPF routing
for i in range(200):
  # Choose the next hop along the optimal path
  try:
      next_hop = optimal_path[i+1]
  
  # Measure the delay
      start = time.time()
  
  # Transmit the packet
      transmit_packet(G,packet_size, next_hop)
  
  # Calculate the delay
      end = time.time()
      delay = end - start
      total_delay += delay
  
  # Add the packet size to the total data transmitted
      total_data += packet_size

# Calculate the average delay
      average_delay = total_delay / 5

# Calculate the overhead
      overhead = total_data / (packet_size * 5)

      print("Average delay:", average_delay)
      print("Overhead:", overhead)
  except:
        pass
