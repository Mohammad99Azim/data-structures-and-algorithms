import sys
sys.path.append('./')

from graph.graph import Graph

def business_trip(graph,array):

    if array == None or array == []:
        raise Exception('no path was given for the Trip')
        
    root = None
    cost = 0
    cities = graph.get_nodes()

    for c in cities:
        if c.value == array[0]:
            root = c

    if root is None:
        return None
        
    for x in range((len(array)-1)):
        neighbors = graph.get_neighbors(root)
        for y in neighbors:
            if y.vertex.value == array[x+1]:
                cost += y.weight
                root = y.vertex
                break
            root = None
        
        if root is None:
            return None
    return cost

    

    

if __name__ == '__main__':

    my_graph = Graph()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")
    c = my_graph.add_node("c")
    d = my_graph.add_node("d")
    e = my_graph.add_node("e")
    f = my_graph.add_node("f")

    my_graph.add_edge(b, a,10)
    my_graph.add_edge(b, d)
    my_graph.add_edge(b, e)
    my_graph.add_edge(b, c,3)

    my_graph.add_edge(c, f,5)

    print(business_trip(my_graph , ["a","b","c","f"]))