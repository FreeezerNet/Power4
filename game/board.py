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
    
    def dropPiece(self, row, col, piece):
        self.board[row][col] = piece   
        
    def verifPlace(self,col) :
        for i in range(self.rows):
            if self.board[i][col] == 0:
                return i   
    
    def winMove(self, piece):
        
        for i in range(self.cols-3):
            for r in range(self.rows):
                if self.board[r][i] == piece and self.board[r][i+1] == piece and self.board[r][i+2] == piece and self.board[r][i+3] == piece:
                    return True 
         
        for i in range(self.cols-3):
            for r in range(self.rows):
                if self.board[r][i] == piece and self.board[r+1][i] == piece and self.board[r+2][i] == piece and self.board[r+3][i] == piece:
                    return True                  
                
        for i in range(self.cols-3):
            for r in range(self.rows-3):
                if self.board[r][i] == piece and self.board[r+1][i+1] == piece and self.board[r+2][i+2] == piece and self.board[r+3][i+3] == piece:
                    return True 
                
        for i in range(self.cols-3):
            for r in range(3,self.rows):
                if self.board[r][i] == piece and self.board[r-1][i+1] == piece and self.board[r-2][i+2] == piece and self.board[r-3][i+3] == piece:
                    return True                
        return False
    
            