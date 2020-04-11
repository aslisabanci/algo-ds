import pytest
from adt_impl.stack import Stack


def test_push_pop():
    s = Stack()
    s.push(6)
    assert s.pop() == 6
    s.push(9)
    s.push(15)
    assert s.pop() == 15
    assert s.pop() == 9


def test_len():
    s = Stack()
    s.push(6)
    s.pop()
    assert len(s) == 0
    s.push(9)
    s.push(15)
    s.pop()
    assert len(s) == 1
    s.push(21)
    assert len(s) == 2


def test_peek():
    s = Stack()
    s.push("jim jarmusch")
    s.push("mike leigh")
    s.push("tony gatlif")
    assert s.peek() == "tony gatlif"
    s.pop()
    assert s.peek() == "mike leigh"
    s.push("zeki demirkubuz")
    assert s.peek() == "zeki demirkubuz"


def test_peek_empty_raiseserror():
    s = Stack()
    with pytest.raises(Exception) as e:
        assert s.peek()
    assert str(e.value) == Stack.EMPTY_STACK_ERR_MSG


def test_pop_empty_raiseserror():
    s = Stack()
    with pytest.raises(Exception) as e:
        assert s.pop()
    assert str(e.value) == Stack.EMPTY_STACK_ERR_MSG
