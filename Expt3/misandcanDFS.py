from collections import deque

m = int(input("No. of Missionaires : "))
c = int(input("No. of Cannibals : "))
b = int(input("Boat size: "))
allpaths = []

def is_valid(state):
    m1, c1, n = state
    m2 = m - m1
    c2 = c - c1
    if m1 < 0  or m2 < 0 or c1 < 0 or c2 < 0:
        return False
    if  (m1 and m1 < c1)  or (m2 and m2 < c2):
        return False
    return True

def generate_successors(state):
    m, c, n = state
    successors = []

    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for action in actions:
        moved_ms, moved_cn =action

        if n == 1:
            new_state = (m - moved_ms, c - moved_cn, 0)
        else:
            new_state = (m + moved_ms, c + moved_cn, 1)
            
        if is_valid(new_state):
            successors.append(new_state)

    return successors

def dfs():
    start_state = (m, c, 1)
    goal_state = (0, 0, 0)

    visited = set()
    q = deque([(start_state,[])])

    while q:
        current_state = q.pop()
        state, path = current_state

        if state in visited:
            continue
        
        path.append(state)
        
        if state == goal_state:
            allpaths.append(path)
            continue

        visited.add(state)

        for successor in generate_successors(state):
            if successor not in visited:
                q.append((successor,path.copy()))


dfs()

if len(allpaths)==0:
    print("No Solutions")
else:
     for p in allpaths:
        print(p)