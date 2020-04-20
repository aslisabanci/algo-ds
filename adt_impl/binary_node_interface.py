from __future__ import annotations
from abc import ABCMeta, abstractmethod


class AbstractBinaryNode(metaclass=ABCMeta):
    @property
    @abstractmethod
    def key(self) -> object:
        pass

    @property
    @abstractmethod
    def left(self) -> AbstractBinaryNode:
        pass

    @property
    @abstractmethod
    def right(self) -> AbstractBinaryNode:
        pass

    def __iter__(self) -> AbstractBinaryNode:
        if self:
            if self.left:
                for node in self.left:
                    yield node
            yield self.key
            if self.right:
                for node in self.right:
                    yield node
