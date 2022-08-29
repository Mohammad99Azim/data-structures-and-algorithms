import sys
sys.path.append('./')
import pytest
from graph_depth_first.graph_depth_first import PreOrder

def test_graph_pre_order(my_graph1):
    actual = my_graph1[0].depth_first(my_graph1[1])
    expect = ['a', 'b', 'c', 'd']
    assert actual == expect

def test_graph_pre_order2(my_graph2):
    actual = my_graph2[0].depth_first(my_graph2[1])
    expect = ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']
    assert actual == expect
    
def test_graph_pre_order3():
    my_graph = PreOrder()
    a = my_graph.add_node("a")
    
    actual = my_graph.depth_first(a)
    expect = ['a']
    assert actual == expect


@pytest.fixture
def my_graph1():
    my_graph = PreOrder()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")
    c = my_graph.add_node("c")
    d = my_graph.add_node("d")

    my_graph.add_edge(a,b)
    my_graph.add_edge(a,d)
    my_graph.add_edge(b,c)
    my_graph.add_edge(b,d)
    return [my_graph,a]

@pytest.fixture
def my_graph2():
    my_graph2 = PreOrder()

    a = my_graph2.add_node("a")
    b = my_graph2.add_node("b")
    c = my_graph2.add_node("c")

    d = my_graph2.add_node("d")
    g = my_graph2.add_node("g")
    e = my_graph2.add_node("e")
    f = my_graph2.add_node("f")
    h = my_graph2.add_node("h")

    my_graph2.add_edge(a,b)
    my_graph2.add_edge(a,d)
    my_graph2.add_edge(b,c)
    my_graph2.add_edge(b,d)
    my_graph2.add_edge(c,g)

    my_graph2.add_edge(d,e)
    my_graph2.add_edge(d,h)
    my_graph2.add_edge(b,f)
    my_graph2.add_edge(f,h)

    return [my_graph2,a]