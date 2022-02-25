import unittest

from src.wincheck import check_win

class TestWin(unittest.TestCase):

    def test_win_cross(self):
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["X"], ["X"], ["X"], ["X"], ["X"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertEqual(check_win(gamegrid, size), "X")
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertEqual(check_win(gamegrid, size), "X")
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertEqual(check_win(gamegrid, size), "X")


    def test_win_o(self):
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["O"], ["O"], ["O"], ["O"], ["O"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertEqual(check_win(gamegrid, size), "O")
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertEqual(check_win(gamegrid, size), "O")
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertEqual(check_win(gamegrid, size), "O")
    
class TestNotWin(unittest.TestCase):
    def test_win_cross(self):
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertFalse(check_win(gamegrid, size))
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["X"], ["X"], ["X"], ["X"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertFalse(check_win(gamegrid, size))
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["X"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["X"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["X"], ["X"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertFalse(check_win(gamegrid, size))
    def test_win_o(self):
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertFalse(check_win(gamegrid, size))
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["O"], ["O"], ["O"], ["O"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertFalse(check_win(gamegrid, size))
        gamegrid, size = [
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["O"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["O"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["O"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["O"], ["O"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["X"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]],
            [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]
            ], 10
        self.assertFalse(check_win(gamegrid, size))

