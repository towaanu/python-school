import math
from queue import Queue

def find_neighbors(graph, vertex):

    if vertex not in graph:
        return None

    return [path["to"] for path in graph[vertex]]

def find_edges(graph, vertex):
    if vertex not in graph:
        return None

    return graph[vertex]

def find_path(graph, frm, to):
    paths = graph[frm]
    return next((p for p in paths if p['to'] == to), None)

def adjacency_matrix(graph):
    vertices_keys = list(graph.keys())
    vertices_number = len(vertices_keys)
    matrix = [[0] * vertices_number for i in range(vertices_number)]

    for i in range(vertices_number):
        current_node_key = vertices_keys[i]
        current_node = graph[current_node_key]
        for j in range(vertices_number):
            key = vertices_keys[j]
            path = find_path(graph, current_node_key, key)
            if path != None:
                matrix[i][j] = path["weight"]

    print(matrix)

def dijkstra_shortest_path(graph, frm, to):
    unvisited_vertices = set(graph.keys())
    vertices_number = len(unvisited_vertices)

    vertices_distance = {}
    previous = {}

    for key in graph.keys():
        vertices_distance[key] = math.inf
        previous[key] = None


    current_vertex = frm
    vertices_distance[current_vertex] = 0
    # While we did not visited every vertex
    while len(unvisited_vertices) > 0:

        # find current vertex 
        min_distance = math.inf
        for unvisited_vertex in unvisited_vertices:
            if min_distance > vertices_distance[unvisited_vertex]:
                min_distance = vertices_distance[unvisited_vertex]
                current_vertex = unvisited_vertex


        current_neighbors = find_edges(graph, current_vertex)
        current_distance = vertices_distance[current_vertex]

        for neighbor in current_neighbors:
            neighbor_vertex = neighbor['to']
            new_distance = neighbor['weight'] + current_distance

            if new_distance < vertices_distance[neighbor_vertex]:
                vertices_distance[neighbor_vertex] = new_distance
                previous[neighbor_vertex] = current_vertex
        
        unvisited_vertices.remove(current_vertex)

    return (vertices_distance, previous)

def breadth_first_search(graph):
    vertices_to_visit = Queue(len(graph.keys()))
    visited_vertex = set()

    first_vertex = list(graph.keys())[0]
    vertices_to_visit.put(first_vertex)

    while not vertices_to_visit.empty():
        current_vertex = vertices_to_visit.get()

        if current_vertex in visited_vertex:
            continue

        print(f"Label: {current_vertex}")

        visited_vertex.add(current_vertex)

        for vertex in find_neighbors(graph, current_vertex):
            vertices_to_visit.put(vertex)

    return None

def depth_first_search(graph):
    vertices_to_visit = list()
    visited_vertex = set()

    first_vertex = list(graph.keys())[0]
    vertices_to_visit.append(first_vertex)

    while vertices_to_visit:
        current_vertex = vertices_to_visit.pop()

        if current_vertex in visited_vertex:
            continue

        print(f"Label: {current_vertex}")

        visited_vertex.add(current_vertex)

        for vertex in find_neighbors(graph, current_vertex):
            vertices_to_visit.append(vertex)

    return None

def bellman_ford(graph, frm, to):
    distance = {}
    keys = graph.keys()
    keys_len = len(keys)
    for key in keys:
        distance[key] = math.inf

    distance[frm] = 0

    for i in range(keys_len):
        for key in keys:
            for edge in find_edges(graph, key):
                to_vertex = edge['to']
                tmp_distance = distance[key] + edge['weight']

                if tmp_distance < distance[to_vertex]:
                    distance[to_vertex] = tmp_distance
    
    return distance


if __name__ == "__main__":

    print("Graph :D")

    my_graph = {
        "A": [
            {"weight": 2, "to": "B"},
            {"weight": 7, "to": "D"},
        ],
        "B": [
            {"weight": 2, "to": "A"},
            {"weight": 11, "to": "C"},
            {"weight": 2, "to": "D"}
        ],
        "C": [
            {"weight": 11, "to": "B"},
            {"weight": 3, "to": "E"}
        ],
        "D": [
            {"weight": 7, "to": "A"},
            {"weight": 2, "to": "B"},
            {"weight": 1, "to": "E"},
        ],
        "E": [
            {"weight": 1, "to": "D"},
            {"weight": 3, "to": "C"}
        ]
    }

    print(dijkstra_shortest_path(my_graph, "A", "E"))
    print(bellman_ford(my_graph, "A", "E"))
    print(find_neighbors(my_graph, "B"))
    print(find_edges(my_graph, "B"))
    adjacency_matrix(my_graph)

    bfs_graph = {
        "A": [
            {"weight": 1, "to": "B"},
            {"weight": 1, "to": "C"},
            {"weight": 1, "to": "D"},
        ],
        "B": [
            {"weight": 1, "to": "E"},
            {"weight": 1, "to": "F"}
        ],
        "C": [],
        "D": [{"weight": 1, "to": "G"}],
        "E": [],
        "F": [],
        "G": [{"weight": 1, "to": "C"}]
    }

    print("BFS")
    print(breadth_first_search(bfs_graph))
    print("DFS")
    print(depth_first_search(bfs_graph))