
from abc import ABCMeta, abstractmethod


class DequeInterface(metaclass=ABCMeta):
    @abstractmethod
    def add_first(self, item:object) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_last(self, item:object) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_first(self) -> object:
        raise NotImplementedError

    @abstractmethod
    def remove_last(self) -> object:
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError