import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7
EMPTY = 0
PLAYER1 = 1
IA = 2
PLAYER_COLORS = {PLAYER1: 'red', IA: 'yellow'}
OUTLAYER = 200

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.current_player = PLAYER1
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=COLS*100+OUTLAYER*2, height=ROWS*100+OUTLAYER, bg='white')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)

        self.draw_board()
        
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def draw_board(self):
        # Draw the blue board area
        self.canvas.create_rectangle(OUTLAYER, OUTLAYER / 2, COLS * 100 + OUTLAYER, ROWS * 100 + OUTLAYER / 2, fill='blue', outline='blue')
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * 100 + 5 + OUTLAYER
                y1 = row * 100 + 5 + OUTLAYER / 2
                x2 = x1 + 90
                y2 = y1 + 90
                self.canvas.create_oval(x1, y1, x2, y2, fill='white', outline='black')
    
    def handle_click(self, event):
        col = (event.x - OUTLAYER) // 100
        if 0 <= col < COLS and self.drop_disc(col):
            if self.check_winner():
                messagebox.showinfo("Connect Four", f"Player {self.current_player} wins!")
                self.reset_game()
            else:
                self.current_player = PLAYER1 if self.current_player == IA else IA

    def drop_disc(self, col):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == EMPTY:
                self.board[row][col] = self.current_player
                x1 = col * 100 + 5 + OUTLAYER
                y1 = row * 100 + 5 + OUTLAYER / 2
                x2 = x1 + 90
                y2 = y1 + 90
                self.canvas.create_oval(x1, y1, x2, y2, fill=PLAYER_COLORS[self.current_player], outline='black')
                return True
        return False
    
    def check_winner(self):
        # Check horizontal, vertical, and diagonal win conditions
        for row in range(ROWS):
            for col in range(COLS - 3):
                if self.board[row][col] == self.current_player and all(self.board[row][col + i] == self.current_player for i in range(1, 4)):
                    return True
        for row in range(ROWS - 3):
            for col in range(COLS):
                if self.board[row][col] == self.current_player and all(self.board[row + i][col] == self.current_player for i in range(1, 4)):
                    return True
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if self.board[row][col] == self.current_player and all(self.board[row + i][col + i] == self.current_player for i in range(1, 4)):
                    return True
        for row in range(3, ROWS):
            for col in range(COLS - 3):
                if self.board[row][col] == self.current_player and all(self.board[row - i][col + i] == self.current_player for i in range(1, 4)):
                    return True
        return False
    
    def reset_game(self):
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.current_player = PLAYER1
        self.canvas.delete("all")
        self.draw_board()

def main():
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()

if __name__ == "__main__":
    main()
