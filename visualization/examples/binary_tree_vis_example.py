from adt_impl.binary_node import BinaryNode
from visualization import binary_tree_visualizer

if __name__ == "__main__":
    b_tree = BinaryNode("root")
    b_tree.insert_left("left1")
    b_tree.insert_left("left2")
    b_tree.insert_left("left3")
    b_tree.insert_right("I know, right?")

    dot = binary_tree_visualizer.visualize(b_tree)
    dot.view(filename="b_tree", directory="./visualization/examples/output")
