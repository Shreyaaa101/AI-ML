import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe - Backtracking")

board = [" "] * 9
buttons = []

# check win
def winner(b, sym):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for x,y,z in wins:
        if b[x]==b[y]==b[z]==sym:
            return True
    return False

def empty_cells(b):
    return [i for i in range(9) if b[i]==" "]

# minimax backtracking
def minimax(b, depth, isMax):
    if winner(b,"O"): return 10-depth
    if winner(b,"X"): return depth-10
    if not empty_cells(b): return 0

    if isMax:  # AI turn
        best = -999
        for i in empty_cells(b):
            b[i] = "O"
            score = minimax(b, depth+1, False)
            b[i] = " "
            best = max(best, score)
        return best
    else:      # human turn
        best = 999
        for i in empty_cells(b):
            b[i] = "X"
            score = minimax(b, depth+1, True)
            b[i] = " "
            best = min(best, score)
        return best

def ai_move():
    best_val = -999
    move = None
    for i in empty_cells(board):
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_val:
            best_val = score
            move = i
    return move

def click(i):
    if board[i]!=" ": return
    board[i] = "X"
    buttons[i].config(text="X", state="disabled")

    if winner(board,"X"):
        end("You Win!")
        return
    if not empty_cells(board):
        end("Draw!")
        return

    ai = ai_move()
    board[ai] = "O"
    buttons[ai].config(text="O", state="disabled")

    if winner(board,"O"):
        end("AI Wins!")
        return
    if not empty_cells(board):
        end("Draw!")

def end(msg):
    lbl = tk.Label(root, text=msg, font=("Arial",16))
    lbl.grid(row=3, column=0, columnspan=3)
    for b in buttons:
        b.config(state="disabled")

# GUI buttons
for i in range(9):
    b = tk.Button(root, text=" ", width=6, height=3,
                  command=lambda i=i: click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

root.mainloop()
