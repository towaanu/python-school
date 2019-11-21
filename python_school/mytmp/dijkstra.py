def get_neighbors(graph, node):
    return graph[node]

def get_item_in_list(items, predicate):
    for i in range(len(items)):
        current_item = items[i]
        if predicate(current_item):
            return (i, current_item)
    
    return (None, None)


def dijkstra(graph, from_node, to_node):
    visited_vertices = set()
    res = []
    came_from = {}

    unvisited_vertices = [{"label": from_node, "weight": 0}]

    while unvisited_vertices:

        current_vertex_index = 0
        current_vertex = unvisited_vertices[current_vertex_index]

        for i in range(len(unvisited_vertices)):
            tmp_vertex = unvisited_vertices[i]
            if tmp_vertex["weight"] < current_vertex["weight"]:
                current_vertex = tmp_vertex
                current_vertex_index = i
        
        unvisited_vertices.pop(current_vertex_index)
        
        neighbors = get_neighbors(graph, current_vertex["label"])

        current_weight = current_vertex["weight"]
        for neighbor in neighbors:

            if neighbor["label"] in visited_vertices:
                continue

            (index, unvisited_vertex) = get_item_in_list(unvisited_vertices, lambda x: x["label"] == neighbor["label"])

            new_weight = current_weight + neighbor["weight"]

            if unvisited_vertex is not None:
                if new_weight < unvisited_vertex["weight"]:
                    unvisited_vertices[index] = {"label": neighbor["label"], "weight": new_weight}
                    came_from[neighbor["label"]] = current_vertex["label"]
            else:
                unvisited_vertices.append({
                    "label": neighbor["label"],
                    "weight": current_weight + neighbor["weight"]
                })
                came_from[neighbor["label"]] = current_vertex["label"]

        
        visited_vertices.add(current_vertex["label"])
        res.append(current_vertex)
    
    return (came_from, res)

        

if __name__ == "__main__":
    print("Hello Dijkstra :D !")

    my_graph = {
        "A": [{"label": "B", "weight": 1}, {"label": "C", "weight": 4}],
        "B": [{"label": "A", "weight": 1}, {"label": "C", "weight": 2}],
        "C": [{"label": "B", "weight": 2}, {"label": "D", "weight": 6}],
        "D": [{"label": "C", "weight": 6}, {"label": "E", "weight": 2}, {"label": "F", "weight": 3}],
        "E": [{"label": "D", "weight": 2}],
        "F": [{"label": "D", "weight": 3}, {"label": "G", "weight": 2}],
        "G": [{"label": "D", "weight": 10}, {"label": "F", "weight": 2}, {"label": "H", "weight": 7}, {"label": "I", "weight": 6}],
        "H": [{"label": "G", "weight": 7}, {"label": "J", "weight": 1}],
        "I": [{"label": "G", "weight": 6}, {"label": "J", "weight": 4}],
        "J": [{"label": "H", "weight": 1}, {"label": "I", "weight": 4}]
    }

    print(dijkstra(my_graph, "A", "D"))