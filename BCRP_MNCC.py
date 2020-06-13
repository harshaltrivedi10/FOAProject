import sys
import math
import networkx as nx
from random import randint

# Calculate MST for G using Prim's algorithm
def primsMST(G):
    MST = []
    edges = set()
    visited = set()
    V = len(G)  # Number of vertices
    u = 0  # Choose first vertex as initial vertex for MST

    # Run prims algorithm until we create an MST that contains every
    # vertex from the graph. Here MST will store edges and max number of
    # edges in MST will be V-1
    while len(MST) != V - 1:
        # Mark source vertex visited
        visited.add(u)
        # Add each edge from this vertex to list of potential edges
        for v in range(V):
            if G[u][v] != 0:
                edges.add((u, v, G[u][v]))

        # Find edge with the smallest weight to a vertex
        # that has not yet been visited
        min_edge = [None, None, float("inf")]
        for e in edges:
            if e[2] < min_edge[2] and e[1] not in visited:
                min_edge = e

        # Remove min weight edge from list of edges
        edges.remove(min_edge)
        # Push min edge to MST
        MST.append(min_edge)
        # Start at new vertex
        u = min_edge[1]

    return MST


# Determine graph for placement of relay nodes using BCRP MNCC algorithm
def get_relay_placement_BCRP_MNCC(MSTEdges, R, budget):
    # create a networkx graph for easier manipulation
    G = nx.Graph()

    total_relay_nodes = 0
    # update edge weights to reflect number of relay nodes required
    # in between 2 nodes of the edge
    for e in MSTEdges:
        relay_nodes_required = math.ceil(e[2] / R) - 1
        G.add_edge(e[0], e[1], weight=relay_nodes_required)
        total_relay_nodes += relay_nodes_required

    # Get sorted edge list so that edge requiring max relay nodes is at the end
    edges = list(sorted(G.edges.data("weight"), key=lambda e: e[2]))
    print("New weights/Edge relay nodes:", edges)
    # Remove max relay node edge until total_relay_nodes is within the given budget
    while total_relay_nodes > budget:
        e = edges.pop()
        G.remove_edge(*e[:2])
        total_relay_nodes -= e[2]

    return G


###############################################
## PROBLEM GENERATION AND TESTING

# Number of nodes is a mandatory parameter
if len(sys.argv) < 2:
    print(
        "Number of nodes is a required parameter for the code.\nUsage: "
        "python algo1.py <num_nodes> <optional:Range> <optional:Budget>"
    )
    exit()
num_nodes = int(sys.argv[1])

# 100x100 Dimension of 2-D plane in which sensor nodes are to be placed
PLANE_SIZE = 100
# Generate num_nodes unique random points in the 2-D plane of
# dimension PLANE_SIZExPLANE_SIZE to place the sensor nodes
points = set()
while len(points) < num_nodes:
    x, y = randint(0, PLANE_SIZE), randint(0, PLANE_SIZE)
    points.add((x, y))
# Convert to list so that points are accessible by index
points = list(points)


# Now generate a complete graph for these points/nodes with edge weights
# as the Euclidean distance between 2 points
graph = [[0 for j in range(num_nodes)] for row in range(num_nodes)]
for i in range(num_nodes):
    for j in range(num_nodes):
        if i == j:
            graph[i][j] = 0
            break
        graph[i][j] = math.sqrt(
            sum([(a - b) ** 2 for a, b in zip(points[i], points[j])])
        )
        graph[j][i] = graph[i][j]

# Pick or optionally get values from command line for
# R: communication range of sensor and relay nodes
# B: budget/constraint on the number of relay nodes that can be deployed
R = 15
if len(sys.argv) > 2:
    R = int(sys.argv[2])
BUDGET = 2
if len(sys.argv) > 3:
    BUDGET = int(sys.argv[3])

###############################################
## HARDCODED GRAPH, R AND B VALUES FOR TESTING
# graph = [
#     [0, 2, 0, 1, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [1, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0],
# ]
# R = 2
# BUDGET = 1
################################################

print("Number of nodes n:", num_nodes, "\tRange R:", R, "\tBudget B:", BUDGET)
# Calculate MST for the generated graph
MSTEdges = primsMST(graph)
print("MST Edges:", MSTEdges)

# Determine graph for placement of relay nodes using BCRP MNCC
placement_graph = get_relay_placement_BCRP_MNCC(MSTEdges, R, BUDGET)
connected_components = list(nx.connected_components(placement_graph))
print("Connected components in the resulting forest:", len(connected_components))
print("Resulting Forest:")
for i, f in enumerate(connected_components):
    print("Tree", i + 1, ":", f)
