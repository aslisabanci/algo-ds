from __future__ import annotations
from adt_impl.binary_node import BinaryNode
from visualization import binary_tree_visualizer
from algo_impl.utilities import math_exp_parser
from adt_impl.stack import Stack


class ExpParseTree(BinaryNode):
    def parse(self, exp: str) -> None:

        stack = Stack()
        tokens = math_exp_parser.tokenize_cumulatively(exp)

        current_tree: ExpParseTree = self
        stack.push(self)

        for t in tokens:
            if t == "(":  # insert a child to the left and move there
                current_tree.insert_left(t)
                stack.push(current_tree)
                current_tree = current_tree.left
            elif t == ")":  # move up to parent
                current_tree = stack.pop()
            elif t in [
                "+",
                "-",
                "*",
                "/",
            ]:  # set the operator for root, insert a child to the right and move there
                current_tree.key = t
                new_node = current_tree.insert_right(t)
                stack.push(current_tree)
                current_tree = current_tree.right
            else:  # set the value to the current tree's root and move up to parent
                current_tree.key = t
                current_tree = stack.pop()

    def appear(self):
        dot = binary_tree_visualizer.visualize(self)
        dot.view(filename="parse_tree", directory="./visualization/examples/output")


if __name__ == "__main__":
    exp = "((((47 + 392) * 50) - 2)) + ((3 - 1) / (136 + 14))"
    parse_tree = ExpParseTree("")
    parse_tree.parse(exp)
    parse_tree.appear()
