def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])

def heuristic(state, goal_state):
    return sum(1 for i in range(9) if state[i] != goal_state[i])

def move(state, direction):
    blank_index = state.index(0)
    new_state = list(state)
    if direction == 'up' and blank_index > 2:
        new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
    elif direction == 'down' and blank_index < 6:
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
    elif direction == 'left' and blank_index % 3 != 0:
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
    elif direction == 'right' and blank_index % 3 != 2:
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
    else:
        return None
    return tuple(new_state)

def generate_neighbors(state):
    neighbors = []
    directions = ['up', 'down', 'left', 'right']
    for direction in directions:
        neighbor = move(state, direction)
        if neighbor is not None:
            neighbors.append(neighbor)
    return neighbors

def solve_puzzle(initial_state, goal_state, max_steps=1000):
    current_state = initial_state
    current_cost = heuristic(initial_state, goal_state)
    steps = 0
    path = [current_state]
    print_state(current_state)
    print("Current heuristic : ",current_cost)
    print()
    while current_cost > 0 and steps < max_steps:
        neighbors = generate_neighbors(current_state)
        best_neighbor = min(neighbors, key=lambda x: heuristic(x, goal_state))
        best_neighbor_cost = heuristic(best_neighbor, goal_state)
        if best_neighbor_cost < current_cost:
            current_state = best_neighbor
            current_cost = best_neighbor_cost

            print_state(current_state)
            print("Current heuristic : ",current_cost)
            print()
            path.append(current_state)
        else:
            print("No solution found")
            break 
        steps += 1


initial_state = tuple(map(int, input("Enter initial state : ").split()))
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solve_puzzle(initial_state, goal_state)
