import random
from board import Board
class Ia:
    def __init__(self):
        self.movesDict = {}
        
    def evaluateMoves(self,board, piece):
        validLocation = [col for col in range(board.cols) if board.locationValid(col)] 
        scores = {col: 0 for col in validLocation}
        
        for col in validLocation:
            row = board.verifPlace(col)
            board.drawPiece(row,col,piece)
            if board.winMove(piece):
                scores[col] += 100
            board.drawPiece(row,col, 0)
        return scores
    
    def bestMove(self, board, piece):
        scores = self.evaluateMoves(board, piece)
        best_score = -float('inf')
        best_cols = []

        for col, score in scores.items():
            if score > best_score:
                best_score = score
                best_cols = [col]
            elif score == best_score:
                best_cols.append(col)

        return random.choice(best_cols) if best_cols else None
                