from collections import deque

ROWS = 3
COLS = 3

def get_zero_index(state):
    for i in range(ROWS):
        for j in range(COLS):
            if state[i][j] == 0:
                return i, j
    return -1, -1

def move_zero(state, index, new_index):
    temp = state[index[0]][index[1]]
    state[index[0]][index[1]] = state[new_index[0]][new_index[1]]
    state[new_index[0]][new_index[1]] = temp
    return state

def provide_next_state(state, goal_state):
    index = get_zero_index(state)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    next_states = []
    for dx, dy in directions:
        new_index = (index[0] + dx, index[1] + dy)
        if 0 <= new_index[0] < ROWS and 0 <= new_index[1] < COLS:
            new_state = [row[:] for row in state]
            new_state = move_zero(new_state, index, new_index)
            next_states.append(new_state)
    return next_states

def solve_8_puzzle(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        if tuple(map(tuple, state)) == tuple(map(tuple, goal_state)):
            return path + [state]
        
        visited.add(tuple(map(tuple, state)))
        next_states = provide_next_state(state, goal_state)
        for next_state in next_states:
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [state]))
    return []

def print_state(state):
    for row in state:
        for val in row:
            print(val, end="   ")
        print()

def main():
    print("Enter 3x3 Matrix")
    initial_state = []
    for _ in range(ROWS):
        row = [int(input()) for _ in range(COLS)]
        initial_state.append(row)

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solution = solve_8_puzzle(initial_state, goal_state)

    if solution:
        print("\nSolution:")
        for idx, state in enumerate(solution):
            print_state(state)
            print()
            if idx < len(solution) - 1:
                print("    ↓")
                print()
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()
