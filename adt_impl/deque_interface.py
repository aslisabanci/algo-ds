
from abc import ABCMeta, abstractmethod


class DequeInterface(metaclass=ABCMeta):
    @abstractmethod
    def add_front(self, item:object) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_rear(self, item:object) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_front(self) -> object:
        raise NotImplementedError

    @abstractmethod
    def remove_rear(self) -> object:
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError