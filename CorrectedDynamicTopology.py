# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:18:31 2022

@author: Muhammad Bilal
"""

import networkx as nx
import random
import math
import matplotlib.pyplot as plt
from matplotlib import pylab


pos = {}
labels = {1:"Source",100:"Destination"}
for i in range(2,99):
    labels[i] = str(i)
for i in range(1, 101):
    pos[i] = (random.randint(0, 1000), random.randint(0, 1000))

def edge_label_maker(G):
    edge_labels = dict()
    eno=0
    for i in range(100):
        for j in range(100):
            try:
                eData=G.get_edge_data(i,j)
                edge_labels[(list(G.edges)[eno])] = round(eData["distance"]/eData["speed"],2)
                eno = eno+1
            except:
                pass
    return edge_labels

def save_graph(graph, file_name,pos,shortest_path,edge_labels):
    # initialze Figure
    plt.figure(num=None, figsize=(100, 100), dpi=200)
    plt.axis('off')
    fig = plt.figure(1)
    nx.draw(G,pos,node_size=1200) #Uncomment this statement to generate all edges
    nx.draw_networkx_edges(G, pos, edgelist=list(
        zip(shortest_path, shortest_path[1:])), edge_color='r', width=5)
   # nx.draw_networkx_nodes(G,pos) Uncomment for shortest path only
    nx.draw_networkx_labels(graph,pos,labels,40)
    nx.draw_networkx_edge_labels(G, pos,edge_labels,font_size = 20) #Uncomment this statement when drawing ALL paths
    cut = 1.00
    xmax = cut * max(xx for xx, yy in pos.values())
    ymax = cut * max(yy for xx, yy in pos.values())
    xmin = cut * min(xx for xx, yy in pos.values())
    ymin = cut * min(yy for xx, yy in pos.values())
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    plt.savefig(file_name, bbox_inches="tight")
    pylab.close()
    del fig


# Assuming that the graph g has nodes and edges entered
SpeedList = []
for j in range(100):
    SpeedList.append(random.uniform(6, 9))

for i in range(20):

    print("\nIteration number ", i+1, ":\n")
    # Create an empty graph
    G = nx.Graph()

    # Add the source vertex and destination vertex
    G.add_node(1)
    G.add_node(100)

    # Add the intermediate vertices
    for i in range(2, 100):
        G.add_node(i)

    # Add edges from the source vertex to the intermediate vertices
    G.add_edge(1, 2, distance=random.uniform(1, 15), speed=SpeedList[2])
    G.add_edge(1, 3, distance=random.uniform(1, 15), speed=SpeedList[3])
    G.add_edge(1, 4, distance=random.uniform(1, 15), speed=SpeedList[4])

    # Add edges from the intermediate vertices to the destination vertex
    G.add_edge(97, 100, distance=random.uniform(1, 15), speed=SpeedList[96])
    G.add_edge(98, 100, distance=random.uniform(1, 15), speed=SpeedList[97])
    G.add_edge(99, 100, distance=random.uniform(1, 15), speed=SpeedList[98])

    for i in range(2, 100):

        for j in range(1, 6):
            if i < 50:
                random_neighbor = random.randint(i+1, i+j)
                if G.degree(random_neighbor) < 5 and G.degree(i) < 5:

                    G.add_edge(i, random_neighbor, distance=random.uniform(1, 15),
                               speed=SpeedList[random_neighbor])
            if i >= 50:
                random_neighbor = random.randint(i-j, i-1)
                if G.degree(random_neighbor) < 5 and G.degree(i) < 5:
                    G.add_edge(i, random_neighbor, distance=random.uniform(1, 15),
                               speed=SpeedList[random_neighbor])
    G.remove_edges_from(nx.selfloop_edges(G))
    edges = G.edges()
    source = 1
    destination = 100
    packetsize=500
    payloadsize= 450
    avgdelay=0

    print("Calculating shortest path")
    for i in range(5):
        # Calculate the total number of paths from the source to the destination
        try:
            shortest_path = nx.shortest_path(G, source, destination)
            print(f"The shortest path is: {shortest_path}")
        except:
            print("No path")

        # Select the optimal path
        min_delay = 0
        optimal_path = None
        try:
            num_hops = nx.shortest_path_length(G, source, destination)
            print(f'Number of hops: {num_hops}')

            min_delay = 0
            for i in range(num_hops):
                try:
                    # Get the edge data for the current edge
                    edge_data = G.get_edge_data(
                        shortest_path[i+1], shortest_path[i+2])
                    # Calculate the delay for the current edge using the distance and speed attributes
                    delay = (edge_data['distance'] / edge_data['speed'])
                    min_delay += delay
                    headersize = packetsize-payloadsize
                    overhead = (headersize)/payloadsize
                except:
                    pass
            print(
                f"The delay from source to destination is: {min_delay:.3f} s")
            print(
                f"The size of a packet is: {packetsize:.3f} bytes")
            print(
                f"The overhead of the network is: {overhead:.3f} bytes")
        except:
            print("Connection fails")

        avgdelay+=min_delay
        
    print( f"The average delay of the network is: {avgdelay/5:.3f} s")

nx.draw(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=list(
    zip(shortest_path, shortest_path[1:])), edge_color='r', width=1)

edge_labels = edge_label_maker(G)

plt.show()
save_graph(G, "my_graph.svg",pos,shortest_path,edge_labels)



# Copy code
