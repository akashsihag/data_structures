graph_elements = {"a": ["b", "c"],
                  "b": ["a", "d"],
                  "c": ["a", "d"],
                  "d": ["e"],
                  "e": ["d"]
                  }

print(graph_elements)


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def get_vertices(self):
        print(list(self.gdict.keys()))

    def get_edges(self):
        edges = []
        for vertex in self.gdict:
            for nxt_vertex in self.gdict[vertex]:
                if {nxt_vertex, vertex} not in edges:
                    edges.append({vertex, nxt_vertex})
        print(edges)

    def add_vertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]


if __name__ == '__main__':
    graph = Graph(graph_elements)
    graph.get_vertices()
    graph.get_edges()
    graph.add_vertex('g')
    graph.get_vertices()
    graph.add_edge({'a', 'c'})
    graph.add_edge({'a', 'g'})
    print(graph.gdict)
    graph.get_edges()
