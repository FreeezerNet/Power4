from ia import Ia
class Player :
    
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.ai = Ia() if is_ai else None
        
    def getMove(self, board):
        if self.is_ai:
            return self.ia.chooseBestMove(board, 2)
        else:
            while True:
                try:
                    col = int(input(f"{self.name}, choisissez une colonne (0-{board.cols-1}): "))
                    if 0 <= col < board.cols and board.locationValid(col):
                        return col
                    else:
                        print("Colonne invalide. Réessayez.")
                except ValueError:
                    print("Entrée invalide. Réessayez.")    