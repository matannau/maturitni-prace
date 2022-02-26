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
        win, symbols = check_win(gamegrid, size)
        self.assertEqual(win, "X")
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
        win, symbols = check_win(gamegrid, size)
        self.assertEqual(win, "X")
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
        win, symbols = check_win(gamegrid, size)
        self.assertEqual(win, "X")


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
        win, symbols = check_win(gamegrid, size)
        self.assertEqual(win, "O")
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
        win, symbols = check_win(gamegrid, size)
        self.assertEqual(win, "O")
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
        win, symbols = check_win(gamegrid, size)
        self.assertEqual(win, "O")
    
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
        win, symbols = check_win(gamegrid, size)
        self.assertFalse(win)
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
        win, symbols = check_win(gamegrid, size)
        self.assertFalse(win)
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
        win, symbols = check_win(gamegrid, size)
        self.assertFalse(win)
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
        win, symbols = check_win(gamegrid, size)
        self.assertFalse(win)
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
        win, symbols = check_win(gamegrid, size)
        self.assertFalse(win)
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
        win, symbols = check_win(gamegrid, size)
        self.assertFalse(win)

