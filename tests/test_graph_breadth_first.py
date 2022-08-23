import sys
sys.path.append('./')
import pytest

from graph_breadth_first.graph_breadth_first import Graph_breadth_first


def test_breadth_first(my_graph):
    actual = my_graph[0].breadth_first(my_graph[1])
    expect = ['a', 'b', 'd', 'e', 'c', 'f']
    assert actual == expect

def test_breadth_first2():
    my_graph = Graph_breadth_first()
    a = my_graph.add_node("a")

    actual = my_graph.breadth_first(a)
    expect = ['a']
    assert actual == expect

def test_breadth_first_Exception():
    my_graph = Graph_breadth_first()
    a = None

    with pytest.raises(Exception) as e:
        my_graph.breadth_first(a)
    assert repr(e) == "<ExceptionInfo Exception('the node given is not valid') tblen=2>"






@pytest.fixture
def my_graph():
    my_graph = Graph_breadth_first()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")
    c = my_graph.add_node("c")
    d = my_graph.add_node("d")
    e = my_graph.add_node("e")
    f = my_graph.add_node("f")

    my_graph.add_edge(b,a)
    my_graph.add_edge(b,d)
    my_graph.add_edge(b,e)
    my_graph.add_edge(b,c)
    
    my_graph.add_edge(c,f)

    return [my_graph,a]
