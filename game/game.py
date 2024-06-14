from ast import While
from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Joueur 1"), Player("Joueur 2", is_ia=True)]
        self.current_player_index = 0
        
    def currentPlayer(self):
        return self.player[self.current_player_index]
    
    def switchPlayer(self):
        self.current_player_index = 1 - self.current_player_index
        
    def playTurn(self):
        player = self.currentPlayer
        print(f"C'est le tour de {player.name}")
        col = player.getMove(self.board)            
        
        if self.board.locationValid(col):
            row = self.board.verifPlace(col)
            self.board.dropPiece(row, col, self.currentPlayer + 1)
            
            if self.board.winMove(self.current_player_index + 1):
                self.bord.printBoard()
                print(f"{player.name} a gagné !")
                return True
            
        else :
            print(f"Colonne invalide")  
        return False  
    
    def startGame(self):
        gameOver = False
        while not gameOver:
            self.board.printBoard()
            gameOver = self.playTurn()
            if not gameOver:
                self.switchPlayer()
        self.board.printBoard()               