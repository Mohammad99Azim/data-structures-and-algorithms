import sys
sys.path.append('./')

import pytest

from graph.graph import Graph
from graph_business_trip.graph_business_trip import *

def test_business_trip(my_graph):
    actual = business_trip(my_graph , ["a","b","c","f"])
    expect = 18
    assert actual == expect

def test_business_trip2(my_graph):
    actual = business_trip(my_graph , ["a","b","f"])
    expect = None
    assert actual == expect

def test_business_trip_wrong_values(my_graph):
    actual = business_trip(my_graph , ["qwe","oo"])
    expect = None
    assert actual == expect

def test_business_trip_no_trip(my_graph):
    
    with pytest.raises(Exception) as e:
        business_trip(my_graph , [])
    assert repr(e) == "<ExceptionInfo Exception('no path was given for the Trip') tblen=2>"







@pytest.fixture
def my_graph():
    my_graph = Graph()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")
    c = my_graph.add_node("c")
    d = my_graph.add_node("d")
    e = my_graph.add_node("e")
    f = my_graph.add_node("f")

    my_graph.add_edge(b, a,10)
    my_graph.add_edge(b, d,4)
    my_graph.add_edge(b, e,4)
    my_graph.add_edge(b, c,3)

    my_graph.add_edge(c, f,5)

    return my_graph