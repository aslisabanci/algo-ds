from __future__ import annotations
from adt_impl.binary_node_interface import AbstractBinaryNode


class BSTNode(AbstractBinaryNode):
    """Implement a binary search tree node, where the reference to the parent is also kept for ease of purpose.
    """

    key: object = None
    val: object = None
    left: BSTNode = None
    right: BSTNode = None
    parent: BSTNode = None

    def __init__(
        self,
        key: object,
        val: object,
        left: BSTNode = None,
        right: BSTNode = None,
        parent: BSTNode = None,
    ):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_left(self) -> bool:
        return False if self.parent == None else self.parent.left == self

    def is_right(self) -> bool:
        return False if self.parent == None else self.parent.right == self

    def is_root(self) -> bool:
        return self.parent == None

    def is_leaf(self) -> bool:  # i.e. has no children
        return not (self.left or self.right)

    def has_a_child(self) -> bool:
        return self.right or self.left

    def has_both_children(self) -> bool:
        return self.right and self.left

    def replace(
        self, key: object, val: object, left: BSTNode = None, right: BSTNode = None
    ) -> None:
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def find_successor(self) -> BSTNode:
        succ = None
        if self.right:
            succ = self.right.find_min()
        else:
            if self.parent:
                if self.is_left():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.find_successor()
                    self.parent.right = self
        return succ

    def find_min(self) -> BSTNode:
        current = self
        while current.left:
            current = current.left
        return current

    def splice_out(self) -> None:
        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_a_child():
            if self.left:
                if self.is_left():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left():
                    self.parent.right = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
