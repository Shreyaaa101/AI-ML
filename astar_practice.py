import heapq

maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0]
]

rows, cols = len(maze), len(maze[0])
start, end = (0,0), (4,4)

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, end):
    open_list = []
    heapq.heappush(open_list, (0, start))  # push start
    
    g_cost = {start: 0}
    parent = {start: None}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == end:
            break
        
        r, c = current
        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr, nc = r + dr, c + dc
            neighbour = (nr, nc)
            
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                new_g = g_cost[current] + 1
                if neighbour not in g_cost or new_g < g_cost[neighbour]:
                    g_cost[neighbour] = new_g
                    f = new_g + heuristic(neighbour, end)
                    heapq.heappush(open_list, (f, neighbour))
                    parent[neighbour] = current
    
    # Reconstruct path
    path = []
    node = end
    while node:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path

print("Shortest path:", astar(start, end))
