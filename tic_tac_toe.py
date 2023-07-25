import tkinter as tk
from tkinter import messagebox

def on_click(row, col):
    if board[row][col] == " ":
        buttons[row][col].config(text=player)
        board[row][col] = player

        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
            root.quit()

        elif is_board_full():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            root.quit()

        toggle_player()

def check_winner():
    # Function to check if there's a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full():
    # Function to check if the board is full (draw)
    for row in board:
        if " " in row:
            return False
    return True

def toggle_player():
    # Function to switch players
    global player
    player = "X" if player == "O" else "O"

# Initialize the game board and player
board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the board
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Start the main event loop
root.mainloop()
