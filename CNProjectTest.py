import networkx as nx
import matplotlib.pyplot as plt


nxG = nx.Graph()

NodeList = [1,2,3,4,5,6,7,8,9,10]

nxG.add_nodes_from(NodeList)

EdgeList = [(1,2,1),(1,3,2),(1,4,4),(1,5,2),(1,6,7),(1,7,5),(1,8,9),(1,9,3),(1,10,5)]

nxG.add_weighted_edges_from(EdgeList)

NodeList2 = [11,12,13,14,15]
nxG.add_nodes_from(NodeList2)

EdgeList2 = [(4,11,1),(4,12,2),(4,13,3),(4,14,4),(4,15,5)]
nxG.add_weighted_edges_from(EdgeList2)

sizes1 = [1000,500,500,500,500,500,500,500,500,500]
sizes2 = [200,200,200,200,200]
pos = nx.spring_layout(nxG)

nx.draw_networkx_nodes(nxG,pos,nodelist = NodeList, node_color = "lightblue",node_shape = "o",node_size = sizes1)
nx.draw_networkx_edges(nxG,pos,nodelist = EdgeList)

nx.draw_networkx_nodes(nxG,pos,nodelist = NodeList2, node_color = "lightcoral",node_shape = "s",node_size = sizes2)
nx.draw_networkx_edges(nxG,pos,nodelist = EdgeList2)

nx.draw_networkx_labels(nxG,pos,font_size = 12)
labels = nx.get_edge_attributes(nxG,'weight')
nx.draw_networkx_edge_labels(nxG,pos,edge_labels=labels)

print(nx.shortest_path(nxG))

plt.savefig("testGraph.png")