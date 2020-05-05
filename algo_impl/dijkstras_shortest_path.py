from adt_impl.graph import Graph, Vertex
from visualization import graph_visualizer
import heapq
from typing import Dict


def calculate_distances(graph: Graph, starting_vertex: Vertex) -> Dict[Vertex, int]:
    distances = {vertex: float("infinity") for vertex in graph.verts.values()}
    distances[starting_vertex] = 0

    prio_queue = [(0, starting_vertex)]
    while len(prio_queue):
        current_dist, current_vert = heapq.heappop(prio_queue)

        if current_dist <= distances[current_vert]:
            for neighbor_vert, weight in current_vert.connections.items():
                distance = current_dist + weight

                if distance < distances[neighbor_vert]:
                    distances[neighbor_vert] = distance
                    heapq.heappush(prio_queue, (distance, neighbor_vert))

    return distances


# TODO: Move to main func
graph = Graph()
graph.add_two_way_edge("U", "V", 2)
graph.add_two_way_edge("U", "X", 1)
graph.add_two_way_edge("V", "X", 2)
graph.add_two_way_edge("U", "W", 5)
graph.add_two_way_edge("V", "W", 3)
graph.add_two_way_edge("W", "X", 3)
graph.add_two_way_edge("W", "Z", 5)
graph.add_two_way_edge("W", "Y", 1)
graph.add_two_way_edge("Z", "Y", 1)
graph.add_two_way_edge("X", "Y", 1)

distances = calculate_distances(graph, graph.verts["X"])
for vertex, dist in distances.items():
    print(f"{vertex.key}: {dist}")
