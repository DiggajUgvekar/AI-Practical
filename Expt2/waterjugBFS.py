from collections import deque


def WaterJugBFS(goal,Left_Capacity,Right_Capacity):
    visited = set()
    
    queue = deque([(0, 0, [(0, 0)])])  #curren state and path

    while queue:    
        Left, Right, path = queue.popleft()
        if Left == goal or Right == goal:
            allpath.append(path)
            continue

        visited.add((Left,Right))

        succ = [(Left_Capacity, Right), (Left, Right_Capacity), (0, Right), (Left, 0)]

        SpaceLeft = Left_Capacity - Left
        if SpaceLeft >= Right:
            succ.append((Left + Right, 0))
        else:
            succ.append((Left_Capacity, Right - SpaceLeft))
            
        SpaceRight = Right_Capacity - Right
        if SpaceRight >= Left:
            succ.append((0, Left + Right))
        else:
            succ.append((Left - SpaceRight, Right_Capacity))


        for s in succ:
            if s not in visited:
                queue.append((s[0], s[1],path + [s] )) #left jug , right jug , path


allpath = []
print("Water Jug Problem (BFS)")
goal = int(input("Enter Goal "))
Left_Capacity = int(input("Enter Capacity of Left Jug : "))
Right_Capacity = int(input("Enter Capacity of Right Jug : "))
WaterJugBFS(goal,Left_Capacity,Right_Capacity)


if len(allpath)==0:
    print("No Solutions")
else:
     for p in allpath:
        print(p)
