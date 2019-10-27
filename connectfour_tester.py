from minimax_connectfour import *
import unittest

class GameBoards():
     
     def __init__(self):
        self.game1 = Game([['-' for i in range(8)] for j in range(8)])
        self.game2 = Game([['-','-','-','-','-','-','-','-'],
                           ['-','-','-','-','-','-','-','-'],
                           ['-','-','-','-','-','-','-','-'],
                           ['-','-','-','-','-','-','-','-'],
                           ['-','-','-','-','-','-','-','-'],
                           ['-','-','-','-','-','-','-','-'],
                           ['-','-','-','-','-','-','-','-'],
                           ['-','-','R','-','-','-','-','-']])

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.g1 = GameBoards().game1
        self.g2 = GameBoards().game2

    def test_moves(self):
        self.assertCountEqual(self.g1.possible_moves(), [0,1,2,3,4,5,6,7])

    def test_neighbor(self):
        self.game1_a = self.g1.neighbor(2,'R')
        self.assertEqual(self.game1_a.grid, self.g2.grid)

    def test_winningstate(self):
        self.assertEqual(self.g1.winning_state(), None)

    def test_tournament(self):
        self.assertGreaterEqual(tournament(50), .7)   # CSC481
        # self.assertGreaterEqual(tournament(50), .85)  # CSC575

if __name__ == '__main__':
    unittest.main(verbosity=2)