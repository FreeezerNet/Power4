import numpy as np

class Board:
    def __init__(self,rows = 6, cols = 7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        
    def locationValid(self,col):
        return self.board[self.rows-1][col] == 0
    
    def printBoard(self):
        print(np.flip(self.board, 0)) 
    
    def drawPiece(self, row, col, piece):
        self.board[row][col] = piece   
        
    def verifPlace(self,col) :
        for i in range(self.rows - 1, -1,-1):
            if self.board[i][col] == 0:
                return i   
        return None    
    
    def winMove(self, piece):
        return self.check_victory(piece) is not None  
    #     for i in range(self.cols-3):
    #         for r in range(self.rows):
    #             if self.board[r][i] == piece and self.board[r][i+1] == piece and self.board[r][i+2] == piece and self.board[r][i+3] == piece:
    #                 return True 
         
    #     for i in range(self.cols-3):
    #         for r in range(self.rows):
    #             if self.board[r][i] == piece and self.board[r+1][i] == piece and self.board[r+2][i] == piece and self.board[r+3][i] == piece:
    #                 return True                  
                
    #     for i in range(self.cols-3):
    #         for r in range(self.rows-3):
    #             if self.board[r][i] == piece and self.board[r+1][i+1] == piece and self.board[r+2][i+2] == piece and self.board[r+3][i+3] == piece:
    #                 return True 
                
    #     for i in range(self.cols-3):
    #         for r in range(3,self.rows):
    #             if self.board[r][i] == piece and self.board[r-1][i+1] == piece and self.board[r-2][i+2] == piece and self.board[r-3][i+3] == piece:
    #                 return True                
    #     return False
    
    def check_victory(self, piece):
        rows = len(self.board)
        cols = len(self.board[0])
        def check_line(start_row, start_col, delta_row, delta_col):
            player = self.board[start_row][start_col]
            if player == 0:
                return False
            for i in range(1, 4):
                r = start_row + delta_row * i
                c = start_col + delta_col * i
                if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.board[r][c] != player:
                    return False
            return True

        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if check_line(row, col, 0, 1):
                    return self.board[row][col]

        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if check_line(row, col, 1, 0):
                    return self.board[row][col]

        # Check diagonals (bottom-left to top-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if check_line(row, col, 1, 1):
                    return self.board[row][col]

        # Check diagonals (top-left to bottom-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if check_line(row, col, -1, 1):
                    return self.board[row][col]

        return None  
            