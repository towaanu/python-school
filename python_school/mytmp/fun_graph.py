from collections import deque
import math
from priority_queue import PriorityQueue

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

def dijkstra(graph, start_vertex):

    vertices_costs = {}

    for vertex in graph.keys():
        vertices_costs[vertex] = math.inf
    
    vertices_costs[start_vertex] = 0
    unvisited_vertices = list(graph.keys())

    came_from = {}
    came_from[start_vertex] = None

    while unvisited_vertices:

        # get min vertex
        min_cost_vertex = unvisited_vertices[0]
        for vertex in unvisited_vertices[1:]:
            if vertices_costs[vertex] < vertices_costs[min_cost_vertex]:
                min_cost_vertex = vertex
        

        current_vertex = min_cost_vertex
        current_vertex_cost = vertices_costs[current_vertex]
        unvisited_vertices.remove(current_vertex)

        for neighbor in graph[current_vertex]:
            (vertex, cost) = neighbor
            new_cost = cost + current_vertex_cost
            if new_cost < vertices_costs[vertex]:
                vertices_costs[vertex] = new_cost
                came_from[vertex] = current_vertex
    
    return (vertices_costs, came_from)

def pqueue_dijkstra(graph, start_vertex):
    
    came_from = {}
    vertices_to_visit = []

    came_from[start_vertex] = None

    vertices_to_visit = PriorityQueue()
    distance = {}

    for vertex in graph.keys():
        distance[vertex] = math.inf
        vertices_to_visit.add(vertex, math.inf)
    
    vertices_to_visit.update_cost(start_vertex, 0)
    distance[start_vertex] = 0

    while not vertices_to_visit.is_empty():

        current_vertex = vertices_to_visit.get()

        for neighbor in graph[current_vertex]:
            (vertex, cost) = neighbor
            new_distance = distance[current_vertex] + cost

            if new_distance < distance[vertex]:
                distance[vertex] = new_distance
                came_from[vertex] = current_vertex
                vertices_to_visit.update_cost(vertex, new_distance)
    
    return (distance, came_from)

def reconstruct_path(came_from, destination):
    current_vertex = destination
    path = []

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = came_from[current_vertex]
    
    return path[::-1]

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

    my_weighted_graph = {
        "A": [("B", 10), ("E", 2)],
        "B": [("A", 10), ("C", 5), ("H", 1)],
        "C": [("B", 5), ("D", 8)],
        "D": [("C", 8), ("G", 4), ("H", 1)],
        "E": [("A", 2), ("F", 3)],
        "F": [("E", 3), ("H", 7)],
        "G": [("D", 4)],
        "H": [("B", 1), ("D", 1), ("F", 7)]
    }

    (costs, came_from) = dijkstra(my_weighted_graph, 'A') 
    path = reconstruct_path(came_from, "G")
    print(f"Dijkstra : {costs}")
    print(f"Dijkstra path : {path}")

    (pqueue_costs, pqueue_came_from) = pqueue_dijkstra(my_weighted_graph, 'A') 
    pqueue_path = reconstruct_path(pqueue_came_from, "G")
    print(f"pqueue_Dijkstra : {pqueue_costs}")
    print(f"pqueue_Dijkstra path : {pqueue_path}")
