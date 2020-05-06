from visualization import graph_visualizer
from adt_impl.graph import Graph

if __name__ == "__main__":
    graph = Graph()
    graph.add_one_way_edge("A", "D", 0)
    graph.add_one_way_edge("A", "B", 0)
    graph.add_one_way_edge("B", "C", 0)
    graph.add_one_way_edge("B", "D", 0)
    graph.add_one_way_edge("D", "E", 0)
    graph.add_one_way_edge("E", "F", 0)
    graph.add_one_way_edge("E", "B", 0)
    graph.add_one_way_edge("F", "C", 0)

    dot = graph_visualizer.visualize(graph)
    dot.view(filename="graph", directory="./visualization/examples/output")
