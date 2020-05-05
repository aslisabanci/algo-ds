from graphviz import Digraph
from adt_impl.graph import Vertex, Graph


def visualize(graph: Graph, dot: Digraph = None) -> None:
    if dot is None:
        dot = Digraph(
            comment="Graph",
            format="png",
            graph_attr={"fixedsize": "false"},
            node_attr={"style": "filled", "fillcolor": "coral", "fontname": "Courier"},
        )

    for vert in graph.verts.values():
        dot.node(name=str(vert), label=str(vert.key))
        for connected_vert, weight in vert.connections.items():
            label = None
            if weight != 0:
                label = str(weight)
            dot.edge(str(vert), str(connected_vert), label=label)

    return dot


from adt_impl.queue import Queue


def bfs(g: Graph, root: Vertex):
    vertices = Queue()
    vertices.enqueue(root)
    visited_vertices = {}
    while len(vertices) > 0:
        current_v = vertices.dequeue()
        for connected_v in current_v.connections.keys():
            if connected_v not in visited_vertices.keys():
                visited_vertices[connected_v] = True
                connected_v.distance_to_bfs_pred = current_v.distance_to_bfs_pred + 1
                connected_v.bfs_pred = current_v
                vertices.enqueue(connected_v)
        visited_vertices[current_v] = True


def traverse(y):
    x = y
    while x.bfs_pred:
        print(x.key)
        x = x.bfs_pred
    print(x.key)


# bucketed_words = {}
# graph = Graph()
# words = [
#     "fail",
#     "foil",
#     "foul",
#     "fool",
#     "cool",
#     "pool",
#     "poll",
#     "pole",
#     "pall",
#     "fall",
#     "pope",
#     "pale",
#     "sale",
#     "sage",
#     "page",
# ]
# for word in words:
#     for i in range(len(word)):
#         bucket = word[:i] + "_" + word[i + 1 :]
#         if bucket in bucketed_words:
#             bucketed_words[bucket].append(word)
#         else:
#             bucketed_words[bucket] = [word]
# # add vertices and edges for words in the same bucket
# for bucket in bucketed_words.keys():
#     for word1 in bucketed_words[bucket]:
#         for word2 in bucketed_words[bucket]:
#             if word1 != word2:
#                 graph.add_edge(word1, word2, 0)

# # dot = visualize(graph)
# # dot.view(filename="graph", directory="./")

# bfs(graph, graph.verts["fool"])
# traverse(graph.verts["sage"])


def DFS(graph: Graph):
    # visited array for storing already visited nodes
    # visited = [False] * len(self.vertex)

    visited_vertices = {}

    # call the recursive helper function
    for v in graph.verts.values():
        if v not in visited_vertices:
            DFSRec(v, visited_vertices)


def DFSRec(startVertex, visited_vertices):
    # mark start vertex as visited
    visited_vertices[startVertex] = True

    print(startVertex.key, end=" ")

    # Recur for all the vertexes that are adjacent to this node
    for i in startVertex.connections.keys():
        if i not in visited_vertices.keys():
            DFSRec(i, visited_vertices)


# TODO: Move to an example script
# dfs_graph = Graph()
# dfs_graph.add_one_way_edge("A", "D", 0)
# dfs_graph.add_one_way_edge("A", "B", 0)
# dfs_graph.add_one_way_edge("B", "C", 0)
# dfs_graph.add_one_way_edge("B", "D", 0)
# dfs_graph.add_one_way_edge("D", "E", 0)
# dfs_graph.add_one_way_edge("E", "F", 0)
# dfs_graph.add_one_way_edge("E", "B", 0)
# dfs_graph.add_one_way_edge("F", "C", 0)
# # dfs_graph.add_edge(2, 3, 0)
# # dfs_graph.add_edge(3, 3, 0)

# dot = visualize(dfs_graph)
# dot.view(filename="graph", directory="./")

# DFS(dfs_graph)
