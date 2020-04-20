from __future__ import annotations
from adt_impl.binary_node_interface import AbstractBinaryNode


class BinaryNode(AbstractBinaryNode):
    key: object = None
    left: BinaryNode = None
    right: BinaryNode = None

    def __init__(self, key: object):
        self.key = key
        self.left: BinaryNode = None
        self.right: BinaryNode = None

    def insert_left(self, key: object) -> None:
        new_node = BinaryNode(key)
        if self.left != None:
            new_node.left = self.left
        self.left = new_node

    def insert_right(self, key: object) -> None:
        new_node = BinaryNode(key)
        if self.right != None:
            new_node.right = self.right
        self.right = new_node
