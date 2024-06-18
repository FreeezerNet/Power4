import tkinter as tk
from tkinter import messagebox
#from game.board import Board # type: ignore
#from game.ia import Ia # type: ignore
from board import Board
from ia import Ia

class ConnectGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Puissance 4")
        
        self.board = Board()
        self.ia = Ia()

        self.buttons = []
        self.createBoard()

    def createBoard(self):
        for row in range(self.board.rows):
            button_row = []
            for col in range(self.board.cols):
                button = tk.Button(self.root, text=" ", width=7, height=3,
                                   command=lambda c=col: self.dropPiece(c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def dropPiece(self, col):
        if self.board.locationValid(col):
            row = self.board.verifPlace(col)
            self.board.dropPiece(row, col, 1)  # Humain
            self.updateBoard()

            if self.board.winMove(1):
                messagebox.showinfo("Puissance 4", "Joueur 1 (Rouge) a gagné !")
                self.resetBoard()
                return

            # L'IA joue
            ia_col = self.ia.bestMove(self.board, 2)  # IA
            self.board.dropPiece(self.board.verifPlace(ia_col), ia_col, 2)
            self.updateBoard()

            if self.board.winMove(2):
                messagebox.showinfo("Puissance 4", "IA (Jaune) a gagné !")
                self.resetBoard()
                return

    def updateBoard(self):
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.board[row][col] == 0:
                    self.buttons[row][col].config(text=" ", bg="white")
                elif self.board.board[row][col] == 1:
                    self.buttons[row][col].config(text="●", bg="red")
                elif self.board.board[row][col] == 2:
                    self.buttons[row][col].config(text="●", bg="yellow")

    def resetBoard(self):
        self.board = Board()
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                self.buttons[row][col].config(text=" ", bg="white")

if __name__ == "__main__":
    print("main lancé")
    root = tk.Tk()
    print("root OK")
    app = ConnectGui(root)
    print("3eme ok")
    root.mainloop()
    print("dernier ok")