from adt_impl.binary_heap import BinaryHeap
import operator


def test_push_pop():
    bh = BinaryHeap(comp_fn=operator.gt)
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

    assert bh.items == [0, 33, 27, 19, 17, 21, 9, 18, 5, 14, 11]
    assert bh.pop() == 33
    assert bh.items == [0, 27, 21, 19, 17, 11, 9, 18, 5, 14]


def test_build():
    bh = BinaryHeap(comp_fn=operator.gt)
    bh.build([11, 21, 5, 9, 27, 14, 18, 19, 33, 17])
    assert bh.items == [0, 33, 27, 18, 21, 17, 5, 14, 9, 19, 11]


def test_pop_from_single_item_heap():
    bh = BinaryHeap(comp_fn=operator.gt)
    bh.build([3])
    assert bh.items == [0, 3]
    assert bh.pop() == 3


def test_push_pop_single_item():
    bh = BinaryHeap(comp_fn=operator.gt)
    bh.push(5)
    assert bh.pop() == 5


def test_push_pop_with_zero():
    bh = BinaryHeap(comp_fn=operator.gt)
    bh.push(25)
    bh.push(7)
    bh.push(13)
    bh.push(14)
    bh.push(127)
    bh.push(2)
    bh.push(0)
    bh.push(35)

    assert bh.items == [0, 127, 35, 13, 25, 14, 2, 0, 7]
    assert bh.pop() == 127
    assert bh.pop() == 35
    assert bh.pop() == 25
    assert bh.pop() == 14
    assert bh.items == [0, 13, 7, 0, 2]
