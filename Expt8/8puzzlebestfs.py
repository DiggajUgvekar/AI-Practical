from queue import PriorityQueue
#1 2 3 7 8 4 6 0 5
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

def solve_puzzle(initial_state, goal_state, max_steps=10):
    current_state = initial_state
    current_cost = heuristic(initial_state, goal_state)
    steps = 0
    path = [current_state]
    print_state(current_state)
    print("Current heuristic : ",current_cost)
    print()
    priority_queue = PriorityQueue()
    priority_queue.put((current_cost, current_state))
    
    while not priority_queue.empty() and steps < max_steps:
        current_cost, current_state = priority_queue.get()
        if current_cost == 0:
            print_state(current_state)
            print("Current heuristic : ",current_cost)
            print()
            print("Goal state reached!")
            break
        
        neighbors = generate_neighbors(current_state)
        for neighbor in neighbors:
            neighbor_cost = heuristic(neighbor, goal_state)
            priority_queue.put((neighbor_cost, neighbor))
        
        if path[-1] != current_state:  # Avoid duplicate states
            path.append(current_state)
            print_state(current_state)
            print("Current heuristic : ",current_cost)
            print()
        
        steps += 1

    if current_cost > 0:
        print("No solution found")

initial_state = tuple(map(int, input("Enter initial state : ").split()))
# inu = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# random.shuffle(inu)
# initial_state = tuple(inu)
goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)

solve_puzzle(initial_state, goal_state)
