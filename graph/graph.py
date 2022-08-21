from collections import deque


class Edge:
    def __init__(self, vertex):
        self.vertex = vertex


class Vertex:
    def __init__(self, value, weight=0):
        self.value = value
        self.weight = weight


class Graph:

    def __init__(self):
        self.__graph_list = {}

    def add_node(self, value):
        '''
        Add the node to __graph_list as key and value it will be an empty list.
        input:value
        return: vertex
        '''
        vertex = Vertex(value)
        self.__graph_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex):
        '''
        if the vertexes are valid will make two instances from Edge class then 
        it will add start_vertex as neighbor for the end_vertex and vice versa.
        input:start_vertex, end_vertex
        return: Nothing
        '''
        if start_vertex not in self.__graph_list or end_vertex not in self.__graph_list:
            raise Exception("vertex should not be None")
        edge = Edge(end_vertex)
        edge2 = Edge(start_vertex)
        self.__graph_list[start_vertex].append(edge)
        self.__graph_list[end_vertex].append(edge2)

    def get_nodes(self):
        '''
        it will return a list of all keys in the graph
        input: Nothing
        return: Nothing

        '''
        return list(self.__graph_list.keys())

    def get_neighbors(self, vertex):
        '''
        will return all the neighbors (have common edge) 
        with the vertex you will pass to it as an argument
        input: vertex
        return:list of  the vertex neighbors
        '''
        return self.__graph_list[vertex]

    def size(self):
        '''
        return the number of vertexes you have in the graph
        input: Nothing
        return: Nothing
        '''
        return len(self.__graph_list)

    def breadth_first(self, root):
        '''
        it will iterate through the graph then 
        return all the values in he vertexes
        input: root (vertex in the graph)
        return list of vertexes values
        '''
        queue = deque()
        visited_set = set()
        finale_results = []

        queue.appendleft(root)
        while queue:
            current = queue.popleft()
            visited_set.add(current)
            finale_results.append(current.value)
            for y in self.__graph_list[current]:
                if y.vertex not in visited_set:
                    queue.append(y.vertex)

        return finale_results


if __name__ == "__main__":
    my_graph = Graph()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")
    c = my_graph.add_node("c")
    d = my_graph.add_node("d")
    e = my_graph.add_node("e")
    f = my_graph.add_node("f")

    my_graph.add_edge(b, a)
    my_graph.add_edge(b, d)
    my_graph.add_edge(b, e)
    my_graph.add_edge(b, c)

    my_graph.add_edge(c, f)

    print(my_graph.breadth_first(a))
