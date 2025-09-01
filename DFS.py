import tkinter as tk

# 0 = clean, 1 = dirty
grid = [[1, 1],
        [1, 1]]

rows, cols = len(grid), len(grid[0])
visited = set()

def dfs(r, c):
    if (r, c) in visited or r<0 or c<0 or r>=rows or c>=cols:
        return
    visited.add((r, c))
    
    if grid[r][c] == 1:  # clean if dirty
        grid[r][c] = 0
        canvas.itemconfig(cells[(r, c)], fill="lightgreen")
    else:
        canvas.itemconfig(cells[(r, c)], fill="white")
    
    root.update(); root.after(500)
    
    # explore neighbors (DFS order)
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        dfs(r+dr, c+dc)

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200); canvas.pack()

cells = {}
for r in range(rows):
    for c in range(cols):
        color = "brown" if grid[r][c]==1 else "white"
        x1, y1 = c*80, r*80
        cells[(r,c)] = canvas.create_rectangle(x1,y1,x1+80,y1+80,fill=color)

root.after(1000, lambda: dfs(0,0))  # start DFS from (0,0)
root.mainloop()
