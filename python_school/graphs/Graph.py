class Graph:
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, label):
        self.graph[label] = []

    def add_edge(self, a, b):
        if a not in self.graph:
            self.graph[a] = []

        if b not in self.graph:
            self.graph[b] = []

        self.graph[a].append(b) 
        self.graph[b].append(a)
    
    def neighbors(self, vertex):
        if vertex not in self.graph:
            return None
        
        return self.graph[vertex]
    
    def vertices(self):
        return list(self.graph.keys())
    
    def edges(self):
        edges = []
        for vertex in self.graph:
            current_neighbors = self.graph[vertex]
            for neighbor_vertex in current_neighbors:
                if (neighbor_vertex, vertex) not in edges:
                    edges.append((vertex, neighbor_vertex))
        return edges

    def __str__(self):
        return str(self.graph)
        
if __name__ == "__main__":
    print("Graph oop :D")
    my_graph = Graph()
    my_graph.add_edge('A', 'B')
    my_graph.add_edge('C', 'D')
    my_graph.add_edge('A', 'D')
    print(my_graph)
    print('neighbors(A) ', my_graph.neighbors('A'))
    print('vertices ', my_graph.vertices())
    print('edges ', my_graph.edges())