from adt_impl.binary_search_tree import BinarySearchTree
from visualization import binary_tree_visualizer

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst[42] = "asli"
    bst[49] = "forty niners"
    bst[1] = "california"
    bst[0] = "sunshine"

    dot = binary_tree_visualizer.visualize(bst.root)
    dot.view(filename="binary_search_tree", directory="./visualization/examples/output")
