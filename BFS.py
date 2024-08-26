from collections import deque

def best_first_search_deque(graph, start, goal, heuristic):
    # Priority queue for exploring nodes based on heuristic values
    queue = deque([(start, heuristic[start])])
    visited = set()
    parent = {start: None}
    cost = {start: 0}

    while queue:
        # Sort queue based on heuristic values to simulate priority queue
        queue = deque(sorted(list(queue), key=lambda x: x[1]))
        current_node, current_heuristic = queue.popleft()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor, edge_cost in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, heuristic[neighbor]))
                parent[neighbor] = current_node
                cost[neighbor] = cost[current_node] + edge_cost

    path = []
    node = goal
    total_cost = cost.get(goal, 0)
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, total_cost

# Example graph with manually assigned costs
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3), ('E', 4)],
    'C': [('F', 5), ('G', 6)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Example heuristic values (assumed for demonstration)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 0,
    'E': 2,
    'F': 3,
    'G': 1
}

start = 'A'
goal = 'D'

path, total_cost = best_first_search_deque(graph, start, goal, heuristic)
print("Best First Search Path:", path)
print("Total Cost:", total_cost)
