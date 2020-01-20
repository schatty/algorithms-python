""" Given a directed graph, design an algorithm to find out whether
there is a route between two nodes. """


graph = {
        "1": set(["1", "2"]),
        "2": set(["6"]),
        "3": set(["4"]),
        "4": set([]),
        "5": set([]),
        "6": set(["5"])
}


def is_connected(graph, start_node, end_node):
    visited = set([])
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        visited.add(node)
        if node == end_node:
            return True
        for ng in graph[node] - visited:
            queue.append(ng)
    return False


print("Is 1 and 5 connected: ", is_connected(graph, "1", "5"))
print("Is 3 and 6 connected: ", is_connected(graph, "3", "6"))
