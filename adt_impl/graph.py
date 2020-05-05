from __future__ import annotations
from typing import Dict


class Vertex:
    def __init__(self, key: str):
        self.connections: Dict[str, Vertex] = {}
        self.key: str = key
        self.distance_to_bfs_pred: int = 0
        self.bfs_pred: Vertex = None

    def connect_to(self, v: Vertex, weight: int) -> None:
        self.connections[v] = weight

    def weight_to(self, v: Vertex) -> int:
        return self.connections[v]

    def __lt__(self, other: Vertex):
        return self.key < other.key


class Graph:
    def __init__(self):
        self.verts: dict = {}

    def _get_or_create_vertex(self, key: str) -> None:
        if key in self.verts:
            return self.verts[key]
        else:
            new_v = Vertex(key)
            self.verts[key] = new_v
            return new_v

    def _connect_edges_one_way(
        self, from_key: str, to_key: str, weight: int
    ) -> (Vertex, Vertex):
        from_v = self._get_or_create_vertex(from_key)
        to_v = self._get_or_create_vertex(to_key)
        from_v.connect_to(to_v, weight)
        return (from_v, to_v)

    def add_one_way_edge(self, from_key: str, to_key: str, weight: int) -> None:
        self._connect_edges_one_way(from_key, to_key, weight)

    def add_two_way_edge(self, from_key: str, to_key: str, weight: int) -> None:
        from_v, to_v = self._connect_edges_one_way(from_key, to_key, weight)
        to_v.connect_to(from_v, weight)
