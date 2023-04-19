# ComputerNetworkProject

This project involves creating and analyzing a network of 100 nodes with random positions, where each node has 5 interfaces connected to 5 other nodes, except the source and destination nodes which have 3 interfaces. The links between the nodes are assigned random values between 1 to 15.

The project calculates the total number of paths from source to destination and selects the optimal path based on delay as a metric. The number of hops for each path is also calculated. Once the optimal path is found, the project transmits five packets of equal size from the source to the destination and calculates the average delay and overhead of the network.

The experiment is executed multiple times (20 times) with different random values to calculate the average and the optimal path. Additionally, the 100 nodes are considered as mobile nodes moving at a constant speed (between 6 to 9 m/s), and the number of attempts a message takes to reach the destination is calculated.

Python, networkX, and Matplotlib libraries are used to implement the project. NetworkX is used to create the network of nodes and calculate the paths between them, while Matplotlib is used to visualize the network topology. The project's implementation involves running the algorithm multiple times to ensure the optimal path is selected and the average is calculated. The results obtained provide insights into the network's performance under different conditions.
