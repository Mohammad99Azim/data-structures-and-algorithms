import sys
sys.path.append('./')

from graph.graph import Graph

class PreOrder(Graph):

    def depth_first(self,root):
        visited = []
        
        def _walk(root):
            visited.append(root.value)
            for x in self.get_neighbors(root):
                if x.vertex.value not in visited:
                    _walk(x.vertex)
        _walk(root)          
        return visited

if __name__ == '__main__':
    my_graph = PreOrder()

    a = my_graph.add_node("a")
    b = my_graph.add_node("b")
    c = my_graph.add_node("c")
    d = my_graph.add_node("d")

    my_graph.add_edge(a,b)
    my_graph.add_edge(a,d)
    my_graph.add_edge(b,c)
    my_graph.add_edge(b,d)

    
    my_graph.depth_first(a)