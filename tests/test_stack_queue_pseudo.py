from stack_queue_pseudo.stacks_queue_pseudo import PseudoQueue
import pytest


def test_pseudo_queue():
    q = PseudoQueue()
    q.enqueue(10)
    assert q.stack2.top.val == 10


def test_pseudo_queue_multiple_values_into_a_queue():
    q = PseudoQueue()
    q.enqueue(10)
    assert q.stack2.top.val == 10 and q.stack1.top.val == 10
    q.enqueue(11)
    assert q.stack2.top.val == 10 and q.stack1.top.val == 11
    q.enqueue(12)
    assert q.stack2.top.val == 10 and q.stack1.top.val == 12
    q.enqueue(13)
    assert q.stack2.top.val == 10 and q.stack1.top.val == 13


def test_dequeue_out_of_a_pseudo_queue(new_queue):
    new_queue.dequeue()
    assert new_queue.stack2.top.val == "B"


def test_pseudo_queue_after_multiple_dequeues(new_queue):
    new_queue.dequeue()
    actual = new_queue.stack2.top.val
    expected = "B"
    assert actual == expected

    new_queue.dequeue()
    actual = new_queue.stack2.top.val
    expected = "C"
    assert actual == expected

    new_queue.dequeue()
    actual = new_queue.stack2.top.val
    expected = "D"
    assert actual == expected


def test_dequeue_on_empty_pseudo_queue_raises_exception():
    q = PseudoQueue()
    with pytest.raises(Exception) as e:
        q.dequeue()
    assert repr(e) == "<ExceptionInfo Exception('The PseudoQueue is Empty') tblen=3>"


@pytest.fixture
def new_queue():
    q = PseudoQueue()

    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    return q
