# FOAProject
Implementation of Two algorithms for the final project of Fundamentals of Algorithms subject.

Problem 1
Budget Constrained Relay Node Placement with Minimum Number of Connected Components (BCRP-MNCC)

Introduction:
The budget constrained relay node placement problem with minimum number of connected components has a goal of deploying the relay nodes in the space that contains various sensor nodes in such a way that this deployment of relay nodes will result in the fewest number of connected components and here the number of relay nodes that can be deployed in the sensor placement space is constrained by a budget. In this problem we are provided with:

    I. The locations od a set of nodes or sensor nodes P = {p1, p2, …., pn} in the Euclidean plane.
    II. The Communication Range of the sensor nodes and relay nodes.
    III. Budget B on the number of relay nodes that can be deployed on the sensing (Euclidean) field in such a way that the resultant structure has minimum number of connected components

Problem Formulation:
The problem here states that when given a set of “n” sensor nodes in an Euclidean plane, Communication Range “R”, a budget on the number of relay nodes “B” and an integer “C”, is it possible to find a set of Q points where the relay nodes can be deployed in such a way that maximum connectedness is achieved and the number of connected components is at most “C”. So, from the given set of “n” sensor nodes P = {p1, p2, …., pn}, we create a graph G = (V, E) where each vi ∈V corresponds to each sensor node pi ∈P. Two nodes vi and vj, corresponding to points pi and pj, have an edge eij between them, if the distance between those nodes is less than or equal to R. Once this graph has been constructed, an augmented graph G = (V’, E’) is constructed by deploying the relay nodes in such a way that the cost of relay nodes is within the budget B and this graph has “maximum connectedness” and has minimum number of connected components. The whole problem is constrained on the budget of the relay nodes, the cost of relay nodes is upper bounded by a constant value “B” that doesn’t let us to deploy any number of relay nodes to achieve “maximum connectedness”. In BRCP-MNCC, a smaller number of connected components is an indicator of a higher level of connectedness of the network.

Solution Approach:
The approach to solve this problem starts with producing an MST on the set of given sensor points and then each edge in the tree is given specific weight. After that a new weight is assigned to the edges according to some specific formula that depends on the communication range. Then based on the budget, edges may be removed starting from the edge that has highest weight, to get the final tree which fulfills all the constraints of the problem statement that is it should have maximum connectedness, it should have minimum number of connected components and the cost of relay nodes should be within the budget B. The algorithm of the method that we will be using to implement the solution is given below:
    1. Create a Minimum Spanning Tree (T) using Prim's Algorithm on the set of terminal points P.
    2. The edge between each pair of vertices in the graph is assigned using the formula: w(e) = ⌈len(e) / R⌉ - 1.
    3. Initialize the total sum of all edges, “sum_edges” with value 0.
    4. Iterate through the whole MST and add the weight of each edge to sum_edge.
    5. While the sum_edges is greater than the budget B do:
        a. Remove_edge = edge with maximum weight in the MST.
        b. Remove the “Remove_edge” in T.
        c. sum_edges = sum_edges – weight (Remove_edge)

Return the resulting tree which satisfies all the constraints of the problem

Actual Implementation:
The program that we implemented takes input as:
(i) Number of terminal points n
(ii) Communication range R (optional, default=15) and
(iii) Budget B (optional, default=2).
We then generate a set of n random points and construct a complete graph where the weight of each edge is the Euclidean distance (L2 distance) between the points. We then find the minimum spanning tree for the graph using Prim’s algorithm.
After that, we run the function get_relay_placement_BRCP_MNCC, which implements logic of the algorithm 4 in the paper. At the end, a forest is returned that satisfies the constraints of Budget Constrained Relay Node Placement with Minimum Number of Connected Component. The code is given below:

Problem 2

Identifying Codes

Introduction:
Though regular graphs are appropriate for finding faulty processors in multiprocessor networks, they are generally hard to realize for wireless networks, especially in indoor settings where there are many reflectors and obstacles. Identifying codes were introduced for finding a way to uniquely identify faulty or defective processors in a system with multiple processors. The problem of construction of an optimal identifying code is known to be NP-complete but this paper suggests a greedy approach to find irreducible identifying codes. This factor of “irreducibility” brings a very special factor into the problem that whenever any codeword is deleted, the resultant code is no longer an identifying code. Thus, the given algorithm always converges, and it converges to a local minimum.

Problem Formulation:
In this problem you introduce following notations and definitions:
    • A graph G = (V, E) where V is a set of vertices and E is a set of edges between the vertices. This graph is said to be distinguishable if it permits an identifying code; otherwise the graph is called indistinguishable graph.
    • We define ρ (u, v) to the number of edges along the shortest path from vertex x to vertex y.
    • The Ball B(x) represents the set of vertices: B(x) = {z ∈ V: ρ (w, x) ≤ 1}.
    • A non-empty set C⊆V which is called a code for the graph G = (V, E). The elements of this graph are called “codewords”. Given a code C, the “identifying code” set of each vertex x ∈V is defined to be: Ic (x) = B(x) ∩ C.
    • A code C is said to be an identifying code if for all x, y ∈V, Ic (x) ≠ Ic (y), that means the identifying codes should be unique for each vertex. Also, this identifying code has the property of being “irreducible” that is deletion of a codeword from that code will result in a code that will not be an identifying code henceforth.

The problem states that if given a distinguishable graph G = (V, E), determine a set C such that C ⊆V such that C is of minimum cardinality and is an identifying code. Thus, to check if a graph is distinguishable, one must only check that there are no two vertices with the same ball. As this problem has been shown to be NP-complete, this paper takes a different approach and considers a more practical modification, given a distinguishable graph G = (V, E), compute a set C such that C ⊆V and C is an irreducible identifying code for G. So, to find a solution to this approach the first step is to check whether the given graph is distinguishable or indistinguishable.

Solution Approach:
Firstly, according to Corollary 1, V is an identifying code for a distinguishable graph G = (V, E). Now the algorithm proceeds to its iterations. At every iteration one codeword is removed or deleted, if this results in an identifying code, the algorithm will proceed; otherwise, the codeword that was removed, it’ll be added back into the code and the algorithm will move onto the next codewords and so on and so forth. Here, each iteration of the algorithm, including the last one, ends with an identifying code of the graph G. This algorithm takes the codewords in the same sequence in the way they are provided as a parameter and the order in which codewords appear significantly affects the output of the algorithm. The good codewords are placed at the end of the sequence that is provided as a parameter.
To get the good codewords, the following cases are considered:
    • If the average degree of the vertices in the graph is low, the good codewords are likely to have a higher degree.
    • If the average degree of the vertices in the graph is high, the good codewords are likely to have a lower degree.

Based on these observations, when the average degree of the graph is greater than half of the number of vertices, we visit the vertices in decreasing order of their degree or else we visit the vertices in increasing order of their degree.

Actual Implementation:
Our program takes a graph as input as edges in the format: v1, v2 and constructs an adjacency list from it. By default, it reads the input from a file named “input3.txt” (included along with the code in the report). Using the adjacency lists, Ball for all vertices are calculated and that is used for verifying if a given code is an identifying code.