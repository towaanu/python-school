
def graph_to_adjacency_matrix(graph):
    graph_keys = list(graph.keys())
    keys_length = len(graph_keys)

    adjacency_matrix = [ [0 for j in range(keys_length)] for i in range(keys_length)]

    for i in range(keys_length):
        current_key = graph_keys[i]
        neighbors = graph[current_key]

        for j in range(keys_length):
            if graph_keys[j] in neighbors:
                adjacency_matrix[i][j] = 1

    return adjacency_matrix

def adjacency_matrix_to_graph(adjacency_matrix, graph_keys):
    graph = {}
    graph_keys_length = len(graph_keys)
    for i in range(len(graph_keys)):
        current_key = graph_keys[i]
        current_row = adjacency_matrix[i]

        graph[current_key] = [graph_keys[k] for k in range(graph_keys_length) if current_row[k] == 1 ]
    
    return graph

def matrix_to_string(matrix):
    rows_str = []
    for row in matrix:
        row_str = ""
        for item in row:
            row_str += f"{item}, "
        rows_str.append(row_str[:-2])
    return "\n".join(rows_str)

if __name__ == "__main__":
    print("Hello graph matrix")
    my_graph = {
        "1": ["1", "2", "5"],
        "2": ["1", "3", "5"],
        "3": ["2", "4"],
        "4": ["3", "5", "6"],
        "5": ["1", "2", "4"],
        "6": ["4"]
    }
    adjacency_matrix = graph_to_adjacency_matrix(my_graph)

    print(matrix_to_string(adjacency_matrix))

    graph_from_matrix = adjacency_matrix_to_graph(adjacency_matrix, ["1", "2", "3", "4", "5", "6"])
    print(graph_from_matrix)