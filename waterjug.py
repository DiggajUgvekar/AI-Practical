from collections import deque


def WaterJugBFS():
    visited = set()
    allpath = []
    queue = deque([(0, 0, [(0, 0)])])  #curren state and path

    while queue:
        Left, Right, path = queue.popleft()
        if Left == 2:
            allpath.append(path)
            continue

        succ = [(4, Right), (Left, 3), (0, Right), (Left, 0)]

        SpaceLeft = 4 - Left
        if SpaceLeft >= Right:
            succ.append((Left + Right, 0))
        else:
            succ.append((4, Right - SpaceLeft))
            
        SpaceRight = 3 - Right
        if SpaceRight >= Left:
            succ.append((0, Left + Right))
        else:
            succ.append((Left - SpaceRight, 3))


        for s in succ:
            if s not in visited:
                visited.add(s)
                queue.append((s[0], s[1],path + [s] )) #left jug , right jug , path

    for p in allpath:
        print(p)


print("Water Jug Problem")
WaterJugBFS()
