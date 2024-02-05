from collections import deque

print('Depth First Search (DFS)')

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)
    matrix.append(row)


def dfs(matrix, start):
    num_vertices = len(matrix)
    visited = [False] * num_vertices
    stack = [start]
    visited[start] = True

    while stack:
        current_node = stack.pop()
        if current_node==0:
            print(f"{current_node}",end="")
        else:
            print(f" -> {current_node}",end="")

        for neighbor in range(num_vertices - 1, -1, -1):
            if matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True



print("\nStarting DFS from node 0")
dfs(matrix, 0)
