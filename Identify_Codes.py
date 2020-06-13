import random
from collections import defaultdict, Counter

# Graph is stored as key-value pairs of vertex and set of its adjacent vertices
graph = defaultdict(set)
# Degree of vertices
degree = Counter()

# Read input graph from file
# Each line is an edge in the format: v1,v2
with open("input3.txt") as in_f:
    for line in in_f:
        v1, v2 = line.strip().split(",")
        # Add edge to graph
        graph[v1].add(v2)
        graph[v2].add(v1)
        # Update degree for each vertex
        degree[v1] += 1
        degree[v2] += 1

# Keys of graph data structure are the vertices
vertices = graph.keys()

# Ball for a vertex represents the set of vertices that are
# adjacent to v together with v.
vertex_ball = [graph[v].union({v}) for v in vertices]


# Determine if given code is an identifying code for the
# given graph represented by all_vertices and their ball
def is_id_code(all_vertices, ball, code):
    duplicate_id_set = False
    # For each vertex, check if any other vertex has the same
    # identifying set as this one
    for i in range(len(all_vertices)):
        if duplicate_id_set:
            break
        id_set_i = ball[i] & code
        for j in range(i + 1, len(all_vertices)):
            id_set_j = ball[j] & code
            if id_set_i == id_set_j:
                duplicate_id_set = True
                break
    # Given code is an identifying code if there are no
    # duplicate idenfying sets in the graph
    return not duplicate_id_set


# Find minimal identifying code for the graph (represented by
# all_vertices and their ball) considering given order of vertices
def find_id_code(all_vertices, ball, vertex_sequence):
    # start with all the vertices in the graph
    code = all_vertices
    if not is_id_code(all_vertices, ball, code):
        return None
    # For each vertex taken in the order provided, determine if
    # removing it still gives us an identifying code
    for v in vertex_sequence:
        new_code = code - {v}
        if is_id_code(all_vertices, ball, new_code):
            code = new_code
    return code


## TEST CASES with different order of vertices
# order_vertices1 = ["f", "g", "d", "e", "a", "b", "c"]
# print("Vertex Sequence:", order_vertices1)
# print("ID Code:", find_id_code(vertices, vertex_ball, order_vertices1), "\n")

# order_vertices2 = ["a", "b", "c", "d", "e", "f", "g"]
# print("Vertex Sequence:", order_vertices2)
# print("ID Code:", find_id_code(vertices, vertex_ball, order_vertices2), "\n")

dec_degree_vertices = [v for v, d in degree.most_common()]
print("Decreasing degree vertex sequence:", dec_degree_vertices)
print("ID Code:", find_id_code(vertices, vertex_ball, dec_degree_vertices), "\n")

inc_degree_vertices = dec_degree_vertices[::-1]
print("Increasing degree vertex sequence:", inc_degree_vertices)
print("ID Code:", find_id_code(vertices, vertex_ball, inc_degree_vertices), "\n")

random_order_vertices = dec_degree_vertices.copy()
random.shuffle(random_order_vertices)
print("Random vertex sequence:", random_order_vertices)
print("ID Code:", find_id_code(vertices, vertex_ball, random_order_vertices), "\n")
