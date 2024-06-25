# ia.py

import random

EMPTY = 0
PLAYER1 = 1
IA = 2

class ConnectFourAI:
    def __init__(self):
        self.scores = {}
        self.current_game_moves = []

    def get_ai_move(self, board, check_winner_func):
        available_columns = [col for col in range(len(board[0])) if board[0][col] == EMPTY]

        # Check if AI can win in the next move
        for col in available_columns:
            row = self.get_next_open_row(board, col)
            if row is not None:
                temp_board = [row[:] for row in board]
                temp_board[row][col] = IA
                if check_winner_func(temp_board, IA):
                    self.record_move(col)
                    return col

        # Check if player can win in the next move and block
        for col in available_columns:
            row = self.get_next_open_row(board, col)
            if row is not None:
                temp_board = [row[:] for row in board]
                temp_board[row][col] = PLAYER1
                if check_winner_func(temp_board, PLAYER1):
                    self.record_move(col)
                    return col

        # Use scores to decide on the move
        max_score = -1
        best_columns = []
        for col in available_columns:
            score = self.scores.get(col, 0)
            if score > max_score:
                max_score = score
                best_columns = [col]
            elif score == max_score:
                best_columns.append(col)

        # If no moves have been learned, choose randomly
        if not best_columns:
            best_columns = available_columns

        chosen_col = random.choice(best_columns)
        self.record_move(chosen_col)
        return chosen_col

    def get_next_open_row(self, board, col):
        for row in reversed(range(len(board))):
            if board[row][col] == EMPTY:
                return row
        return None

    def record_move(self, col):
        self.current_game_moves.append(col)

    def end_game(self, result):
        # Result is 1 for a win, -1 for a loss, and 0 for a draw
        adjustment = 1 if result == 1 else -1
        for col in self.current_game_moves:
            if col in self.scores:
                self.scores[col] += adjustment
            else:
                self.scores[col] = adjustment
        self.current_game_moves = []

    def check_winner(self, board, player):
        ROWS = len(board)
        COLS = len(board[0])
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
