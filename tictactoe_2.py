import tkinter as tk
from tkinter import messagebox
import random

class SOS:
    def __init__(self, master):
        self.master = master
        self.master.title("SOS Oyunu")

        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = []

        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(master, text=" ", width=6, height=3, font=("Helvetica", 24), command=lambda i=i, j=j: self.move(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def move(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = "X"
            self.buttons[i][j].configure(text="X", state="disabled")
            if not self.check_win("X"):
                self.computer_move()

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = "O"
            self.buttons[i][j].configure(text="O", state="disabled")
            self.check_win("O")
        else:
            messagebox.showinfo("Oyun Bitti", "Berabere!")

    def check_win(self, player):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                self.game_over(player, [(i, 0), (i, 1), (i, 2)])
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                self.game_over(player, [(0, i), (1, i), (2, i)])
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            self.game_over(player, [(0, 0), (1, 1), (2, 2)])
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            self.game_over(player, [(0, 2), (1, 1), (2, 0)])
            return True
        return False

    def game_over(self, player, winning_positions):
        for pos in winning_positions:
            i, j = pos
            self.buttons[i][j].configure(fg="red")  # Highlight winning characters in red
        messagebox.showinfo("Oyun Bitti!", f"{player} kazandı!")

        # Disable all buttons
        for row in self.buttons:
            for button in row:
                button.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = SOS(root)
    root.mainloop()
