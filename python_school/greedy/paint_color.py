def color_graph(graph):
    nb_color = 1

    colors = {}

    for vertex in graph.keys():
        neighbor_colors = [colors[neighbor] for neighbor in graph[vertex] if neighbor in colors]

        new_color = 1
        while new_color <= nb_color and new_color in neighbor_colors:
            new_color += 1
        
        if new_color > nb_color:
            nb_color += 1
        
        colors[vertex] = new_color
    
    return (nb_color, colors)



if __name__ == "__main__":
    print("paint color")

    graph = {
        "A": ["B"],
        "B": ["B", "C", "D"],
        "C": ["B", "D"],
        "D": ["B", "C"]
    }

    print(color_graph(graph))