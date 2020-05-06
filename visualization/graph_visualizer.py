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
