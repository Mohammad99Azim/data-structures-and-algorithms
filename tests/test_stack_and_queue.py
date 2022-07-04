import pytest
from stack_and_queue.stack_queue import Queue, Stack


def test_push_onto_a_stack(new_stack):
    new_stack.push(99)
    assert new_stack.top.val == 99


def test_push_multiple_values(new_stack):
    new_stack.push(90)
    assert new_stack.top.val == 90
    new_stack.push(91)
    assert new_stack.top.val == 91
    new_stack.push(92)
    assert new_stack.top.val == 92
    new_stack.push(93)
    assert new_stack.top.val == 93
    new_stack.push(94)
    assert new_stack.top.val == 94


def test_pop_off_the_stack(new_stack):
    new_stack.push(98)
    new_stack.push(99)
    assert new_stack.top.val == 99
    new_stack.pop()
    assert new_stack.top.val == 98


def test_empty_a_stack_after_multiple_pops(new_stack):
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()

    assert new_stack.is_empty()


def test_peek_next_item_on_the_stack(new_stack):
    assert new_stack.peek() == 14


def test_instantiate_an_empty_stack():
    my_stack = Stack()
    assert my_stack.top is None


def test_k_greater_than_length():
    with pytest.raises(Exception) as e:
        s = Stack()
        s.pop()

    assert (
            repr(e)
            == """<ExceptionInfo Exception("Can\'t pop the Stack is Empty") tblen=2>"""
    )


###   Queue Tests  ###

def test_enqueue_into_a_queue():
    q = Queue()
    q.enqueue(10)
    assert q.front.val == 10


def test_enqueue_multiple_values_into_a_queue():
    q = Queue()
    q.enqueue(10)
    assert q.front.val == 10
    q.enqueue(11)
    assert q.rare.val == 11
    q.enqueue(12)
    assert q.rare.val == 12
    q.enqueue(13)
    assert q.rare.val == 13


def test_dequeue_out_of_a_queue_the_expected_value(new_queue):
    actual = new_queue.dequeue()
    expected = "A"
    assert actual == expected


def test_peek_into_a_queue(new_queue):
    actual = new_queue.peek()
    expected = "A"
    assert actual == expected


def test_empty_a_queue_after_multiple_dequeues(new_queue):
    actual = new_queue.dequeue()
    expected = "A"
    assert actual == expected

    actual = new_queue.dequeue()
    expected = "B"
    assert actual == expected

    actual = new_queue.dequeue()
    expected = "C"
    assert actual == expected


def test_instantiate_an_empty_queue():
    q = Queue()
    assert q.front is None


def test_peek_on_empty_queue_raises_exception():
    q = Queue()
    with pytest.raises(Exception) as e:
        q.dequeue()
    assert repr(e) == '<ExceptionInfo Exception("Can\'t dequeue The Queue is Empty") tblen=2>'


@pytest.fixture
def new_stack():
    new_stack = Stack()

    new_stack.push(10)
    new_stack.push(11)
    new_stack.push(12)
    new_stack.push(13)
    new_stack.push(14)
    return new_stack


@pytest.fixture
def new_queue():
    q = Queue()

    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.enqueue("E")
    return q
