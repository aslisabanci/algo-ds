from adt_impl.graph import Graph, Vertex
from collections import defaultdict
import heapq


def create_spanning_tree(graph: Graph, starting_vertex: Vertex):
    min_spanning_tree = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph.verts[starting_vertex.key].connections.items()
    ]
    heapq.heapify(edges)
    print(edges)

    while edges:
        cost, from_v, to_v = heapq.heappop(edges)
        if to_v not in visited:
            visited.add(to_v)
            min_spanning_tree[from_v].add(to_v)
            for neighbor_vert, cost in graph.verts[to_v.key].connections.items():
                if neighbor_vert not in visited:
                    heapq.heappush(edges, (cost, to_v, neighbor_vert))
        else:
            print(
                f"Skipping visited vertex {to_v.key}, connected from:{from_v.key} with cost:{cost}"
            )

    return min_spanning_tree


# TODO: Move to main func
graph = Graph()
graph.add_two_way_edge("A", "B", 2)
graph.add_two_way_edge("A", "C", 3)
graph.add_two_way_edge("B", "C", 1)
graph.add_two_way_edge("B", "D", 1)
graph.add_two_way_edge("B", "E", 4)
graph.add_two_way_edge("C", "F", 5)
graph.add_two_way_edge("D", "E", 1)
graph.add_two_way_edge("E", "F", 1)
graph.add_two_way_edge("F", "G", 1)

min_spanning_tree = dict(create_spanning_tree(graph, graph.verts["A"]))
for vert, connections in min_spanning_tree.items():
    print(f"{vert.key}: {[conn.key for conn in connections]}")
