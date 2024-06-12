def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            # Add unvisited neighbors to the stack
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)

        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

    return visited


# Example graph1:
graph1 = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D"],
    "F": ["D"]
}

print(dfs(graph1, "A"))