""" Given graph and two nodes find all possible paths inbetween. """

graph = {"A": set(["B", "C"]),
         "B": set(["A", "D", "E"]),
         "C": set(["A", "F"]),
         "D": set(["B"]),
         "E": set(["B", "F"]),
         "F": set(["C", "E"])}

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


print(list(dfs_paths(graph, "C", "F")))
