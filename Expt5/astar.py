import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.heuristic = {}
    
    def add_node(self, value, heuristic=0):
        self.nodes.add(value)
        self.heuristic[value] = heuristic
     
    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))
    
    def get_neighbors(self, node):
        if node in self.edges:
            return self.edges[node]
        else:
            return []
    
    def a_star(self, start, goal):
        frontier = [(0, start)]
        came_from = {} #The came-from dictionary records the predecessors of each state along the shortest path found so far.
        cost_so_far = {start: 0}   #This dictionary keeps track of the cost of the shortest path found so far to each state.
        
        while frontier:
            current_cost, current_node = heapq.heappop(frontier)
            
            if current_node == goal:
                path = []
                while current_node in came_from:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.append(start)
                path.reverse()
                
                # Calculate total cost
                total_cost = 0
                for i in range(len(path) - 1):
                    total_cost += self.get_cost(path[i], path[i+1])
                
                return path, total_cost
            
            for neighbor, cost in self.get_neighbors(current_node):
                new_cost = cost_so_far[current_node] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic[neighbor]
                    #f(n) = g(n) + h(n)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current_node
        
        return None, None
    
    def get_cost(self, from_node, to_node):
        for neighbor, cost in self.edges[from_node]:
            if neighbor == to_node:
                return cost
        return None


graph = Graph()
graph.add_node('S', heuristic=14)
graph.add_node('A', heuristic=11)
graph.add_node('B', heuristic=10)
graph.add_node('C', heuristic=8)
graph.add_node('D', heuristic=12)
graph.add_node('E', heuristic=5)
graph.add_node('F', heuristic=12)
graph.add_node('H', heuristic=8)
graph.add_node('I', heuristic=10)
graph.add_node('J', heuristic=8)
graph.add_node('K', heuristic=6)
graph.add_node('L', heuristic=10)
graph.add_node('M', heuristic=7)
graph.add_node('N', heuristic=4)
graph.add_node('O', heuristic=8)
graph.add_node('P', heuristic=5)
graph.add_node('Q', heuristic=1)
graph.add_node('R', heuristic=6)
graph.add_node('T', heuristic=2)
graph.add_node('G', heuristic=0)

graph.add_edge('S', 'D', 25)
graph.add_edge('D', 'A', 32)
graph.add_edge('D', 'F', 24)
graph.add_edge('A', 'B', 11)
graph.add_edge('A', 'H', 36)
graph.add_edge('B', 'C', 24)
graph.add_edge('B', 'K', 42)
graph.add_edge('C', 'E', 40)
graph.add_edge('E', 'K', 32)
graph.add_edge('K', 'H', 28)
graph.add_edge('K', 'N', 27)
graph.add_edge('K', 'Q', 62)
graph.add_edge('H', 'N', 44)
graph.add_edge('N', 'Q', 32)
graph.add_edge('N', 'G', 42)
graph.add_edge('T', 'G', 32)
graph.add_edge('R', 'T', 52)
graph.add_edge('O', 'R', 27)
graph.add_edge('L', 'O', 26)
graph.add_edge('C', 'D', 3)
graph.add_edge('I', 'L', 21)
graph.add_edge('I', 'M', 32)
graph.add_edge('J', 'M', 20)
graph.add_edge('M', 'P', 23)
graph.add_edge('H', 'J', 22)
graph.add_edge('D', 'I', 26)
graph.add_edge('F', 'L', 27)

start_node = 'S'
goal_node = 'G'

path, total_cost = graph.a_star(start_node, goal_node)
if path:
    print(" -> ".join(path))
    print("Total Cost:", total_cost)
else:
    print("No path found")
