import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
from game.ia import ConnectFourAI
from game.canvas_drawer import ConnectFourCanvas

ROWS = 6
COLS = 7
EMPTY = 0
PLAYER1 = 1
IA = 2
PLAYER_COLORS = {PLAYER1: 'red', IA: 'yellow'}
CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'src', 'connect_four_games.csv')

class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.init_csv_file()
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.current_player = PLAYER1
        self.moves = []  # List to store the sequence of moves
        self.ai = ConnectFourAI(self.moves)
        self.canvas_drawer = ConnectFourCanvas(root, self.board, self.handle_click)
        self.create_widgets()
        

    def create_widgets(self):
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def init_csv_file(self):
        # Ensure the directory structure exists
        src_dir = os.path.join(os.path.dirname(__file__), '..', 'src')
        if not os.path.exists(src_dir):
            os.makedirs(src_dir)

        # Check if CSV file exists, if not, create it
        if not os.path.exists(CSV_FILE):
            print(f"Creating CSV file at: {CSV_FILE}")
            df = pd.DataFrame(columns=["Moves", "Winner"])
            df.to_csv(CSV_FILE, sep=';', index=False)

    def handle_click(self, col):
        if self.current_player == PLAYER1:
            if self.drop_disc(col):
                self.moves.append(col)  # Register the move
                if self.check_winner(self.board, self.current_player):
                    messagebox.showinfo("Connect Four", f"Player {self.current_player} wins!")
                    self.log_game_result("Player 1")
                    self.reset_game()
                else:
                    self.current_player = IA
                    self.root.after(500, self.ia_move)  # Delay AI move for better visualization

    def drop_disc(self, col):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == EMPTY:
                self.board[row][col] = self.current_player
                self.canvas_drawer.animate_drop(col, row, PLAYER_COLORS[self.current_player])
                return True
        return False

    def ia_move(self):
        col = self.ai.get_ai_move(self.board, self.check_winner, self.moves)
        if col is not None and self.drop_disc(col):
            self.moves.append(col)  # Register the move
            if self.check_winner(self.board, self.current_player):
                messagebox.showinfo("Connect Four", f"Player {self.current_player} wins!")
                self.log_game_result("AI")
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

    def log_game_result(self, winner):
        df = pd.read_csv(CSV_FILE, sep=';')

        # Create a new row with a flat list of moves
        new_row = pd.DataFrame({"Moves": [self.moves], "Winner": [winner]})

        # Concatenate the new row with the existing DataFrame
        df = pd.concat([df, new_row], ignore_index=True)

        # Save the updated DataFrame to CSV
        df.to_csv(CSV_FILE, sep=';', index=False)


    def reset_game(self):
        if not self.moves:
            self.log_game_result("Tie")
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.current_player = PLAYER1
        self.moves = []  # Reset the moves list
        self.canvas_drawer.reset()

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()