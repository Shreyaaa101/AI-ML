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
    # Manhattan distance (grid-based movement)
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, end):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f, node)
    
    g = {start: 0}       # cost from start
    parent = {start: None}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == end:
            break
        
        r, c = current
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr, nc = r+dr, c+dc
            neighbor = (nr, nc)
            
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                new_g = g[current] + 1
                if neighbor not in g or new_g < g[neighbor]:
                    g[neighbor] = new_g
                    f = new_g + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f, neighbor))
                    parent[neighbor] = current
    
    # reconstruct path
    path = []
    node = end
    while node:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path

# Run
path = astar(start, end)
print("Shortest path using A*:", path)
