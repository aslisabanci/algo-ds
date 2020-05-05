from adt_impl.binary_node import BinaryNode
from visualization import binary_tree_visualizer

b_tree = BinaryNode("root")
b_tree.insert_left("dav1")
b_tree.insert_left("dav2")
b_tree.insert_left("dav3")
b_tree.insert_right("right dav?")

dot = binary_tree_visualizer.visualize(b_tree)
dot.view(filename="parse_tree", directory="./")
