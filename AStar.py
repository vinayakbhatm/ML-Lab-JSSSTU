from collections import deque

def a_star_search_deque(graph, start, goal, heuristic, cost):
    # Queue for exploring nodes
    queue = deque([(start, 0 + heuristic[start])])
    visited = set()
    g_cost = {start: 0}
    parent = {start: None}

    while queue:
        # Sort queue based on f-cost to simulate priority queue
        queue = deque(sorted(list(queue), key=lambda x: x[1]))
        current_node, current_f_cost = queue.popleft()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor in graph[current_node]:
            new_cost = g_cost[current_node] + cost[(current_node, neighbor)]
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                queue.append((neighbor, f_cost))
                parent[neighbor] = current_node

    path = []
    node = goal
    total_cost = g_cost.get(goal, 0)
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, total_cost

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Example heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 0,
    'E': 2,
    'F': 3,
    'G': 1
}

# Example costs between nodes
cost = {
    ('A', 'B'): 1,
    ('A', 'C'): 1,
    ('B', 'D'): 1,
    ('B', 'E'): 3,
    ('C', 'F'): 5,
    ('C', 'G'): 2
}

start = 'A'
goal = 'D'

path, total_cost = a_star_search_deque(graph, start, goal, heuristic, cost)
print("A* Search Path:", path)
print("Total Cost:", total_cost)
