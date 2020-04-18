from adt_impl.binary_heap import BinaryHeap
import operator


def test_push_pop():
    bh = BinaryHeap(comp_fn=operator.lt)
    bh.push(5)
    bh.push(9)
    bh.push(11)
    bh.push(14)
    bh.push(18)
    bh.push(19)
    bh.push(21)
    bh.push(33)
    bh.push(17)
    bh.push(27)

    assert bh.items == [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
    assert bh.pop() == 5
    assert bh.items == [0, 9, 14, 11, 17, 18, 19, 21, 33, 27]


def test_build():
    bh = BinaryHeap(comp_fn=operator.lt)
    bh.build([11, 21, 5, 9, 27, 14, 18, 19, 33, 17])
    assert bh.items == [0, 5, 9, 11, 19, 17, 14, 18, 21, 33, 27]


def test_build_single_item():
    bh = BinaryHeap(comp_fn=operator.lt)
    bh.build([3])
    assert bh.items == [0, 3]


def test_pop_from_single_item_heap():
    bh = BinaryHeap(comp_fn=operator.lt)
    bh.build([3])
    assert bh.items == [0, 3]
    assert bh.pop() == 3


def test_push_pop_single_item():
    bh = BinaryHeap(comp_fn=operator.lt)
    bh.push(5)
    assert bh.pop() == 5


def test_pop_from_empty_heap():
    bh = BinaryHeap(comp_fn=operator.lt)
    assert bh.pop() == None


def test_pop_until_empty():
    bh = BinaryHeap(comp_fn=operator.lt)
    bh.push(5)
    assert bh.pop() == 5
    assert bh.pop() == None


def test_push_pop_with_zero():
    bh = BinaryHeap(comp_fn=operator.lt)
    bh.push(25)
    bh.push(7)
    bh.push(13)
    bh.push(14)
    bh.push(127)
    bh.push(2)
    bh.push(0)
    bh.push(35)

    assert bh.items == [0, 0, 14, 2, 25, 127, 13, 7, 35]
    assert bh.pop() == 0
    assert bh.pop() == 2
    assert bh.pop() == 7
    assert bh.pop() == 13
    assert bh.items == [0, 14, 25, 35, 127]
