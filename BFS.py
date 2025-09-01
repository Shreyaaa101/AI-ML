import tkinter as tk
from collections import deque

# 1 = wall, 0 = free
maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0]
]

rows, cols = len(maze), len(maze[0])
start, end = (0,0), (4,4)

root = tk.Tk()
canvas = tk.Canvas(root, width=cols*60, height=rows*60)
canvas.pack()

cells = {}
for r in range(rows):
    for c in range(cols):
        color = "black" if maze[r][c] == 1 else "white"
        x1,y1,x2,y2 = c*60, r*60, (c+1)*60, (r+1)*60
        cells[(r,c)] = canvas.create_rectangle(x1,y1,x2,y2,fill=color,outline="gray")

# Mark start and end
canvas.itemconfig(cells[start], fill="green")
canvas.itemconfig(cells[end], fill="red")

def bfs(start, end):
    q = deque([start])
    
    parent = {start: None}
    visited = {start}

    while q:
        r,c = q.popleft()
        if (r,c) == end: break

        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr,nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                parent[(nr,nc)] = (r,c)
                q.append((nr,nc))
                canvas.itemconfig(cells[(nr,nc)], fill="lightblue")
                root.update(); root.after(100)

    # Reconstruct path
    path=[]
    node=end
    while node:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    for p in path:
        if p not in [start,end]:
            canvas.itemconfig(cells[p], fill="yellow")
            root.update(); root.after(100)

root.after(1000, lambda: bfs(start,end))
root.mainloop()
