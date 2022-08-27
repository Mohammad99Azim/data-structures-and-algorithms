from pickle import TRUE
import sys
sys.path.append("./")

import pytest
from graph.graph import Edge,Vertex,Graph

# Node can be successfully added to the graph
def test_add_to_graph(my_graph):
    node = my_graph.add_node("g")

    actual = my_graph._Graph__graph_list[node] == []
    expected = True

    assert actual == expected 

# An edge can be successfully added to the graph
def test_add_edge_to_graph(my_graph):
    node1 = my_graph.add_node("g")
    node2 = my_graph.add_node("h")

    my_graph.add_edge(node1,node2)
    edge = Edge(node2)

    actual = my_graph._Graph__graph_list[node1][0].vertex == node2
    expected = True

    assert actual == expected 


# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes_from_graph():
    my_graph = Graph()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")

    actual = my_graph.get_nodes()
    
    expected = [a,b]

    
    assert actual == expected 

# All appropriate neighbors can be retrieved from the graph
def test_get_neighbors():
    my_graph = Graph()

    node1 = my_graph.add_node("g")
    node2 = my_graph.add_node("h")

    my_graph.add_edge(node1,node2)
   
    actual = my_graph.get_neighbors(node1)[0].vertex
    expect = node2
    assert actual == expect


# Neighbors are returned with the weight between nodes included
def test_get_neighbors_weight():
    my_graph = Graph()

    node1 = my_graph.add_node("g")
    node2 = my_graph.add_node("h")

    my_graph.add_edge(node1,node2)
   
    actual = my_graph.get_neighbors(node1)[0].weight
    expect = 0
    assert actual == expect



# The proper size is returned, representing the number of nodes in the graph
def test_size(my_graph):
    actual = my_graph.size()
    expect = 6

    assert actual == expect
    


# A graph with only one node and edge can be properly returned
def test_graph_one_node():
    my_graph = Graph()

    node1 = my_graph.add_node("g")

    my_graph.add_edge(node1,node1)
    
    actual = node1 in my_graph._Graph__graph_list
    expect = True
    assert actual == expect


# An empty graph properly returns null
    my_graph = Graph()
    
    actual = my_graph._Graph__graph_list == {}
    expect = True
    assert actual == expect



@pytest.fixture
def my_graph():
    my_graph = Graph()

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

    return my_graph