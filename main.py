import tkinter as tk
from tkinter import messagebox
from game.ia import ConnectFourAI

ROWS = 6
COLS = 7
EMPTY = 0
PLAYER1 = 1
IA = 2
PLAYER_COLORS = {PLAYER1: 'red', IA: 'yellow'}
OUTLAYER = 200
ANIMATION_SPEED = 20  # Speed of the drop animation in milliseconds

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.current_player = PLAYER1
        self.ai = ConnectFourAI()
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
        if self.current_player == PLAYER1:
            col = (event.x - OUTLAYER) // 100
            if 0 <= col < COLS and self.drop_disc(col):
                if self.check_winner(self.board, self.current_player):
                    messagebox.showinfo("Connect Four", f"Player {self.current_player} wins!")
                    self.ai.end_game(-1)  # AI loses
                    self.reset_game()
                else:
                    self.current_player = IA
                    self.root.after(500, self.ia_move)  # Delay AI move for better visualization

    def drop_disc(self, col):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == EMPTY:
                self.board[row][col] = self.current_player
                self.animate_drop(col, row, PLAYER_COLORS[self.current_player])
                return True
        return False

    def animate_drop(self, col, row, color):
        x1 = col * 100 + 5 + OUTLAYER
        x2 = x1 + 90
        y1 = 5 + OUTLAYER / 2
        y2 = y1 + 90

        oval = self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline='black')

        def step_animation(current_y):
            if current_y < row * 100 + 5 + OUTLAYER / 2:
                self.canvas.move(oval, 0, 10)
                self.root.after(ANIMATION_SPEED, step_animation, current_y + 10)
            else:
                self.canvas.move(oval, 0, row * 100 + 5 + OUTLAYER / 2 - current_y)  # Correct position if overshoot

        step_animation(y1)

    def ia_move(self):
        col = self.ai.get_ai_move(self.board, self.check_winner)
        if col is not None and self.drop_disc(col):
            if self.check_winner(self.board, self.current_player):
                messagebox.showinfo("Connect Four", f"Player {self.current_player} wins!")
                self.ai.end_game(1)  # AI wins
                self.reset_game()
            else:
                self.current_player = PLAYER1

    def check_winner(self, board, player):
        # Check horizontal, vertical, and diagonal win conditions
        for row in range(ROWS):
            for col in range(COLS - 3):
                if board[row][col] == player and all(board[row][col + i] == player for i in range(1, 4)):
                    return True
        for row in range(ROWS - 3):
            for col in range(COLS):
                if board[row][col] == player and all(board[row + i][col] == player for i in range(1, 4)):
                    return True
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if board[row][col] == player and all(board[row + i][col + i] == player for i in range(1, 4)):
                    return True
        for row in range(3, ROWS):
            for col in range(COLS - 3):
                if board[row][col] == player and all(board[row - i][col + i] == player for i in range(1, 4)):
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
