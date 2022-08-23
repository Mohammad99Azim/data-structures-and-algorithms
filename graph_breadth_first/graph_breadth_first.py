import sys
sys.path.append('./')

from collections import deque
from graph.graph import Graph

class Graph_breadth_first(Graph):

    def breadth_first(self, root):
            '''
            it will iterate through the graph then 
            return all the values in he vertexes
            input: root (vertex in the graph)
            return list of vertexes values
            '''
            try:
                val =root.value
                weight =root.weight
            except:
                raise Exception("the node given is not valid")
 

            queue = deque()
            visited_set = set()
            finale_results = []

            queue.appendleft(root)
            while queue:
                current = queue.popleft()
                visited_set.add(current)
                finale_results.append(current.value)
                for y in self._Graph__graph_list[current]:
                    if y.vertex not in visited_set:
                        queue.append(y.vertex)

            return finale_results

if __name__ == '__main__':
    my_graph = Graph_breadth_first()

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
