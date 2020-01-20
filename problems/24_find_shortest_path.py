graph = {
        "A": set(["C", "B"]),
        "B": set(["A", "D", "E"]),
        "C": set(["A", "D", "F"]),
        "D": set(["C", "B", "G"]),
        "E": set(["B", "F"]),
        "F": set(["C", "E"]),
        "G": set(["D"])
}


def get_shortest_path(graph, start_node, end_node):
    visited = set([])
    queue = [[start_node]]
    while queue:
        path = list(queue.pop(0))
        visited.add(tuple(path))
        node = path[-1]
        if node == end_node:
            return path
        for ng in graph[node]:
            next_path = tuple(path + [ng])
            if next_path not in visited:
                queue.append(next_path)


print("Shortest path: ", get_shortest_path(graph, "A", "G"))
