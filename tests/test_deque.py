from adt_impl.list_deque import ListDeque
from adt_impl.linkedlist_deque import LinkedListDeque, TailedLinkListDeque
from adt_impl.doublelinkedlist_deque import DoubleLinkedListDeque
import pytest

deques = [
    ListDeque(),
    LinkedListDeque(),
    TailedLinkListDeque(),
    DoubleLinkedListDeque(),
]


@pytest.mark.parametrize("deque", deques)
def test_add_front_remove_front(deque):
    deque.add_front("first")
    deque.add_front("second")
    assert deque.remove_front() == "second"


@pytest.mark.parametrize("deque", deques)
def test_add_front_remove_rear(deque):
    deque.add_front("first")
    deque.add_front("second")
    assert deque.remove_rear() == "first"


@pytest.mark.parametrize("deque", deques)
def test_add_rear_remove_front(deque):
    deque.add_rear("first")
    deque.add_rear("second")
    assert deque.remove_front() == "first"


@pytest.mark.parametrize("deque", deques)
def test_add_rear_remove_rear(deque):
    deque.add_rear("first")
    deque.add_rear("second")
    assert deque.remove_rear() == "second"


@pytest.mark.parametrize("deque", deques)
def test_add_remove_consecutively(deque):
    deque.add_front(2)
    deque.add_front(6)
    assert deque.remove_front() == 6
    deque.add_rear(11)
    deque.add_rear(12)
    deque.add_rear(32)
    deque.add_rear(42)
    assert deque.remove_front() == 2
    assert deque.remove_rear() == 42
    assert deque.remove_rear() == 32


@pytest.mark.parametrize("deque", deques)
def test_is_not_empty(deque):
    deque.add_rear("first")
    deque.add_rear("second")
    deque.add_front("third")
    deque.remove_rear()
    assert deque.is_empty() == False


@pytest.mark.parametrize("deque", deques)
def test_is_empty(deque):
    deque.add_rear("first")
    deque.add_rear("second")
    deque.add_front("third")
    deque.remove_rear()
    deque.remove_rear()
    deque.remove_front()
    assert deque.is_empty() == True
