from graphviz import Digraph
from adt_impl.binary_node_interface import AbstractBinaryNode
from adt_impl.binary_node import BinaryNode
from adt_impl.binary_search_tree import BinarySearchTree


def visualize(node: AbstractBinaryNode, dot: Digraph = None) -> None:
    if dot is None:
        dot = Digraph(
            "g", node_attr={"shape": "egg", "height": ".1", "fontname": "Courier"},
        )
        dot.node(name=str(node), label=str(node.key))

    if node.left:
        dot.node(name=str(node.left), label=str(node.left.key))
        dot.edge(str(node), str(node.left))
        dot = visualize(node.left, dot=dot)

    if node.right:
        dot.node(name=str(node.right), label=str(node.right.key))
        dot.edge(str(node), str(node.right))
        dot = visualize(node.right, dot=dot)

    return dot
