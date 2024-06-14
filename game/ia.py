from board import Board
class Ia:
    def __init__(self):
        self.movesDict = {}
        
    def evaluateMoves(self,board, piece):
        validLocation = [col for col in range(board.cols) if board.locationValid(col)] 
        scores = {col: 0 for col in validLocation}
        
        for col in validLocation:
            row = board.verifPlace(col)
            board.dropPiece(row,col,piece)
            if board.winMove(piece):
                scores[col] += 100
            board.dropPiece(row,col, 0)
        return scores
    def bestMove(self, board, piece):
        scores = self.evaluateMoves(board, piece)
        bestCol = max(scores, key=scores.get)
        return bestCol        