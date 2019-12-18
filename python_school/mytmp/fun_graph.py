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
