from collections import deque
rows = 3
cols = 3
print("Enter 3x3 Matrix")

initial_state = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input())
        row.append(element)
    initial_state.append(row)
    
	

def calclulateHeuristic(state, goal_state):
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                heuristic += 1
    return heuristic

def getZeroIndex(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return [i, j]
    return -1

def moveZeroUp(state, index):
    temp = state[index[0]][index[1]]
    state[index[0]][index[1]] = state[index[0] - 1][index[1]]
    state[index[0] - 1][index[1]] = temp
    return state

def moveZeroDown(state, index):
    temp = state[index[0]][index[1]]
    state[index[0]][index[1]] = state[index[0] + 1][index[1]]
    state[index[0] + 1][index[1]] = temp
    return state

def moveZeroLeft(state, index):
    temp = state[index[0]][index[1]]
    state[index[0]][index[1]] = state[index[0]][index[1] - 1]
    state[index[0]][index[1] - 1] = temp
    return state

def moveZeroRight(state, index):
    temp = state[index[0]][index[1]]
    state[index[0]][index[1]] = state[index[0]][index[1] + 1]
    state[index[0]][index[1] + 1] = temp
    return state

def provideNextState(state, goal_state):
    global global_heuristic, global_state
    mutable_state = [row[:] for row in state]
    index = getZeroIndex(mutable_state)
    if index[0] != 0:
        state1 = moveZeroUp([row[:] for row in mutable_state], index)
        h1 = calclulateHeuristic(state1, goal_state)
        if h1 < global_heuristic:
            global_heuristic = h1
            global_state = state1
    if index[0] != 2:
        state2 = moveZeroDown([row[:] for row in mutable_state], index)
        h2 = calclulateHeuristic(state2, goal_state)
        if h2 < global_heuristic:
            global_heuristic = h2
            global_state = state2
    if index[1] != 0:
        state3 = moveZeroLeft([row[:] for row in mutable_state], index)
        h3 = calclulateHeuristic(state3, goal_state)
        if h3 < global_heuristic:
            global_heuristic = h3
            global_state = state3
    if index[1] != 2:
        state4 = moveZeroRight([row[:] for row in mutable_state], index)
        h4 = calclulateHeuristic(state4, goal_state)
        if h4 < global_heuristic:
            global_heuristic = h4
            global_state = state4
    return global_state

def is_empty(arr):
    return not any(arr)

def solve8Puzzle(initial_state, goal_state):
    all_paths = []
    queue = deque([(initial_state, [])])
    global global_heuristic, global_state
    global_heuristic = calclulateHeuristic(initial_state, goal_state)
    global_state = initial_state
    
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            path.append(state)
            all_paths.append(path.copy())
            return all_paths
        
        parent_value = global_heuristic
        next_state = provideNextState(state, goal_state)
        
        if is_empty(next_state) or parent_value == global_heuristic:
            print("the solution cant move further, its stuck")
            return all_paths
        
        queue.append((next_state, path + [next_state]))
    return [[]]




goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

all_paths = solve8Puzzle(initial_state, goal_state)
print("Initial State")
for i in initial_state:
	for j in i:
		print(j,end="   ")
	print()
	
print("Solution :")
if not is_empty(all_paths):
    for pat in all_paths:
    	for i in pat:
    		for j in i:
    			for k in j:
    				print(k,end="   ")
    			print()
    		print("\n")
else:
    print("No solution found.")		    

