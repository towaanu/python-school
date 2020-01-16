from collections import deque

def find_neighbors(graph, vertex):
    return graph[vertex]

# Parcours en largeurs d'abord
def bfs(graph, start_vertex):

    vertices_to_visit = deque()
    vertices_to_visit.append(start_vertex)
    visited_vertex = set()
    visited_vertex.add(start_vertex)

    while vertices_to_visit:

        current_vertex = vertices_to_visit.popleft()
        print(f"[BFS] Vertex : {current_vertex}")

        for neighbor in find_neighbors(graph, current_vertex):
            if neighbor not in visited_vertex:
                visited_vertex.add(neighbor)
                vertices_to_visit.append(neighbor)
        
# Parcours en profondeur d'abord
def dfs(graph, start_vertex):

    vertices_to_visit = list()
    vertices_to_visit.append(start_vertex)

    visited_vertices = set()
    visited_vertices.add(start_vertex)

    while vertices_to_visit:
        current_vertex = vertices_to_visit.pop()
        print(f"[DFS] Vertex : {current_vertex}")

        for neighbor in find_neighbors(graph, current_vertex):
            if neighbor not in visited_vertices:
                visited_vertices.add(neighbor)
                vertices_to_visit.append(neighbor)

# Verifier, si le graph contient des cycles
def is_cycle(graph):
    vertices = list(graph.keys())

    if not vertices:
        return False
    
    vertices_to_visit = []
    start_vertex = vertices[0]
    vertices_to_visit.append(start_vertex)
    parent_vertices = {}
    parent_vertices[start_vertex] = None

    while vertices_to_visit:
        current_vertex = vertices_to_visit.pop()

        # On regarde tous les voisins
        for neighbor in graph[current_vertex]:

            if parent_vertices[current_vertex] == neighbor:
                continue

            # Si un voisin est déjà dans la pile
            # Il y a un cycle
            if neighbor in vertices_to_visit:
                return True
            
            parent_vertices[neighbor] = current_vertex
            vertices_to_visit.append(neighbor)
    
    return False


# def dfs_is_cycle(graph, start_vertex):

if __name__ == "__main__":
    print("Hello Functional graph ! :D")

    my_graph = {
        "A": ["B", "C", "D"],
        "B": ["A", "E", "F"],
        "C": ["A", "G"],
        "D": ["A", "H", "I"],
        "E": ["B"],
        "F": ["B"],
        "G": ["C", "J"],
        "H": ["D"],
        "I": ["D"],
        "J": ["G"]
    }

    bfs(my_graph, "A")
    dfs(my_graph, "A")

    no_cycle_graph = {
        "A": ["B", "D"],
        "B": ["A", "C"],
        "C": ["B"],
        "D": ["A"]
    }

    print(f"[is_cycle] {is_cycle(no_cycle_graph)}")
