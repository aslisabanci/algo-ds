from adt_impl.graph import Graph, Vertex
from algo_impl import graph_traversal
from visualization import graph_visualizer


def build_word_ladder(words: list) -> Graph:
    bucketed_words = {}
    graph = Graph()

    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i + 1 :]
            if bucket in bucketed_words:
                bucketed_words[bucket].append(word)
            else:
                bucketed_words[bucket] = [word]

    # add vertices and two-way edges between words in the same bucket
    for bucket in bucketed_words.keys():
        for word1 in bucketed_words[bucket]:
            for word2 in bucketed_words[bucket]:
                if word1 != word2:
                    graph.add_one_way_edge(word1, word2, 0)

    return graph


if __name__ == "__main__":
    words = [
        "fail",
        "foil",
        "foul",
        "fool",
        "cool",
        "pool",
        "poll",
        "pole",
        "pall",
        "fall",
        "pope",
        "pale",
        "sale",
        "sage",
        "page",
    ]

    word_ladder_graph = build_word_ladder(words)

    dot = graph_visualizer.visualize(word_ladder_graph)
    dot.view(filename="graph", directory="./visualization/examples/output")

    graph_traversal.traverse_breadth_first(
        word_ladder_graph, word_ladder_graph.verts["fool"]
    )

    final_vertex = word_ladder_graph.verts["sage"]
    while final_vertex.bfs_pred:
        print(final_vertex.key)
        final_vertex = final_vertex.bfs_pred
    print(final_vertex.key)
