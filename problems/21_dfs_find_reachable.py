"""Given graph print out all accessible elements from current
node via Depth First search. """


graph = {"A": set(["B", "C"]),
         "B": set(["A", "D", "E"]),
         "C": set(["A", "F"]),
         "D": set(["B"]),
         "E": set(["B", "F"]),
         "F": set(["C", "E"])}


def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


start_node = "A"
print("All nodes visited: ", dfs(graph, start_node))
