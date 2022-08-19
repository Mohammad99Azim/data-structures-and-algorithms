from collections import deque

class Edge:
    def __init__(self,vertex):
        self.vertex =vertex


class Vertex:
    def __init__(self,value,weight=0):
        self.value = value
        self.weight = weight

class Graph: 

    def __init__(self):
        self.__graph_list = {}


    def add_node(self,value):
        vertex = Vertex(value)
        self.__graph_list[vertex] = []
        return vertex
    
    def add_edge(self,start_vertex,end_vertex):
        if start_vertex not in self.__graph_list or end_vertex not in self.__graph_list:
            raise Exception("vertex should not be None")
        edge = Edge(end_vertex)
        edge2 = Edge(start_vertex)
        self.__graph_list[start_vertex].append(edge)
        self.__graph_list[end_vertex].append(edge2)

    def get_nodes(self):
        return list(self.__graph_list.keys())

    def get_neighbors(self,vertex):
        return self.__graph_list[vertex]
    
    def size(self):
        return len(self.__graph_list)

    def breadth_first(self , root):
        queue = deque()
        visited_set =set()
        finale_results =[]

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

    my_graph.add_edge(b,a)
    my_graph.add_edge(b,d)
    my_graph.add_edge(b,e)
    my_graph.add_edge(b,c)
    
    my_graph.add_edge(c,f)

 
    
    print(my_graph.breadth_first(a))
