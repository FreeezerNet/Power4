import unittest
from board import Board
from ia import Ia
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.ia = Ia()
        self.game = Game()

    def testBoardCreation(self):
        self.assertIsInstance(self.board, Board)
        self.assertEqual(self.board.rows, 6)
        self.assertEqual(self.board.cols, 7)

    def testDropPiece(self):
        self.board.drop_piece(0, 3, 1)
        self.assertEqual(self.board.board[0][3], 1)

    def testWinningMove(self):
        self.board.drop_piece(0, 3, 1)
        self.board.drop_piece(1, 3, 1)
        self.board.drop_piece(2, 3, 1)
        self.board.drop_piece(3, 3, 1)
        self.assertTrue(self.board.winMove(1))

    def testIaChooseBestMove(self):
        best_move = self.Ia.bestMove(self.board, 1)
        self.assertIn(best_move, range(self.board.cols))

    def test_game_play(self):
        pass
    
    if __name__ =="__main__":
        unittest.main()