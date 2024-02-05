from collections import deque

print('Breadth First Search (BFS)')
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)
    matrix.append(row)


def bfs(matrix, start):
    num_vertices = len(matrix)
    visited = [False] * num_vertices
    queue = deque([start])
    visited[start] = True

    while queue:
        current_node = queue.popleft()
        if current_node==0:
            print(f"{current_node}",end="")
        else:
            print(f" -> {current_node}",end="")
        for neighbor in range(num_vertices):
            if matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


print("\nStarting BFS from node 0")
bfs(matrix, 0)
