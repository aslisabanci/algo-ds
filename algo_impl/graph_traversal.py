from adt_impl.queue import Queue
from adt_impl.graph import Graph, Vertex


def traverse_breadth_first(g: Graph, root: Vertex):
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


def _rec_depth_first(startVertex, visited_vertices):
    visited_vertices[startVertex] = True
    print(startVertex.key, end=" ")

    for i in startVertex.connections.keys():
        if i not in visited_vertices.keys():
            _rec_depth_first(i, visited_vertices)


def traverse_depth_first(graph: Graph):
    visited_vertices = {}
    for v in graph.verts.values():
        if v not in visited_vertices:
            _rec_depth_first(v, visited_vertices)
