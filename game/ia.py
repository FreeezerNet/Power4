import pandas as pd
import os
import random
import ast

EMPTY = 0
PLAYER1 = 1
IA = 2
CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'src', 'connect_four_games.csv')

class ConnectFourAI:
    def __init__(self, currentMoves):
        self.currentMoves = currentMoves
        self.data_base = pd.read_csv(CSV_FILE, sep=';')
        self.scores = {col: 0 for col in range(7)}  # Initialize scores for all columns

    def get_ai_move(self, board, check_winner_func, currentMoves):
        self.currentMoves = currentMoves
        available_columns = [col for col in range(len(board[0])) if board[0][col] == EMPTY]

        # Reset scores for each move
        self.scores.clear()
        self.scores = {col: 0 for col in range(7)}

        # Learn from past games
        self.learn_from_past_games()
        self.learn_from_player_past_games()

        self.print_scores()

        # Check if AI can win in the next move
        for col in available_columns:
            row = self.get_next_open_row(board, col)
            if row is not None:
                temp_board = [row[:] for row in board]
                temp_board[row][col] = IA
                if check_winner_func(temp_board, IA):
                    return col

        # Check if player can win in the next move and block
        for col in available_columns:
            row = self.get_next_open_row(board, col)
            if row is not None:
                temp_board = [row[:] for row in board]
                temp_board[row][col] = PLAYER1
                if check_winner_func(temp_board, PLAYER1):
                    return col

        # Determine the best column to play
        best_column = self.choose_best_column(available_columns)

        # Print scores before making the move
        

        return best_column

    def choose_best_column(self, available_columns):
        max_score = -float('inf')
        best_columns = []
        for col in available_columns:
            if self.scores[col] > max_score:
                max_score = self.scores[col]
                best_columns = [col]
            elif self.scores[col] == max_score:
                best_columns.append(col)
        return random.choice(best_columns) if best_columns else random.choice(available_columns)

    def learn_from_past_games(self):
        if not os.path.exists(CSV_FILE):
            return

        df = pd.read_csv(CSV_FILE, sep=';')
        for index, row in df.iterrows():
            gameMoves = ast.literal_eval(row['Moves'])
            winner = row['Winner']
            print(gameMoves)
            print(self.currentMoves)
            print(gameMoves[:min(len(gameMoves), len(self.currentMoves))])
            if self.currentMoves == gameMoves[:min(len(gameMoves), len(self.currentMoves))]:
                value = 0
                if winner == 'AI':
                    value = 1
                elif winner == 'Player1':
                    value = -1
                self.scores[gameMoves[len(self.currentMoves)]] += value
                print(value)
            

    def learn_from_player_past_games(self):
        if not os.path.exists(CSV_FILE):
            return

        df = pd.read_csv(CSV_FILE, sep=';')
        for index, row in df.iterrows():
            gameMoves = ast.literal_eval(row['Moves'])
            winner = row['Winner']
            if self.currentMoves == gameMoves[:min(len(gameMoves), len(self.currentMoves))]:
                value = 0
                if winner == 'Player1':
                    value = 1
                elif winner == 'AI':
                    value = -1
                self.scores[gameMoves[len(self.currentMoves)+1]] += value

    def print_scores(self):
        print("Scores:")
        for col in range(7):  # Assuming 7 columns in the Connect Four game
            print(f"Column {col}: {self.scores.get(col)}")
        print("-----------------")

    def get_next_open_row(self, board, col):
        for row in reversed(range(len(board))):
            if board[row][col] == EMPTY:
                return row
        return None

    def check_winner(self, board, player):
        ROWS = len(board)
        COLS = len(board[0])
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