import heapq
import tkinter as tk

# Maze (0 = free, 1 = wall)
maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0]
]

rows, cols = len(maze), len(maze[0])
start, end = (0,0), (4,4)
cell_size = 80  # pixel size for each square

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, end):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g = {start: 0}
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

# Run A*
path = astar(start, end)
print("Shortest path using A*:", path)

# ---- Tkinter GUI ----
root = tk.Tk()
root.title("A* Pathfinding")

canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size)
canvas.pack()

# Draw maze
for r in range(rows):
    for c in range(cols):
        color = "white" if maze[r][c] == 0 else "black"
        x1, y1 = c*cell_size, r*cell_size
        x2, y2 = x1+cell_size, y1+cell_size
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

# Highlight path
for (r,c) in path:
    x1, y1 = c*cell_size, r*cell_size
    x2, y2 = x1+cell_size, y1+cell_size
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="gray")

# Mark start and end
sr, sc = start
er, ec = end
canvas.create_rectangle(sc*cell_size, sr*cell_size,
                        sc*cell_size+cell_size, sr*cell_size+cell_size,
                        fill="green")
canvas.create_rectangle(ec*cell_size, er*cell_size,
                        ec*cell_size+cell_size, er*cell_size+cell_size,
                        fill="red")

root.mainloop()
