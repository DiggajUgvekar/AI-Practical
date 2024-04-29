from queue import PriorityQueue

def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        cost, node = pq.get()
        if node == goal:
            return True  # Goal reached
        if node not in visited:
            visited.add(node)
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    pq.put((neighbor_cost, neighbor))
    return False  # Goal not reachable

# Example usage:
graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 9), ('E', 2)],
    'C': [('F', 7)],
    'D': [],
    'E': [('G', 1)],
    'F': [('H', 5)],
    'G': [],
    'H': []
}

start_node = 'A'
goal_node = 'G'
print(best_first_search(graph, start_node, goal_node))
