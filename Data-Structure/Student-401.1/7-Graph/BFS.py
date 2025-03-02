from collections import deque


def bfs_iterative(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            # Enqueue unvisited neighbors
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

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

print(bfs_iterative(graph1, "A"))
