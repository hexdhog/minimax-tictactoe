import unittest

from tictactoe.board import *

class BoardTests(unittest.TestCase):
    def test_piece_str(self):
        self.assertEqual(str(Piece.EMPTY), ' ', 'Piece.EMPTY\'s value is not \' \'')
        self.assertEqual(str(Piece.CROSS), 'X', 'Piece.CROSS\'s value is not \'X\'')
        self.assertEqual(str(Piece.NOUGHT), 'O', 'Piece.NOUGHT\'s value is not \'O\'')

    def test_board_init(self):
        board = Board()
        self.assertEqual(len(board.data), Board.DEFAULT_SIZE * Board.DEFAULT_SIZE)
        self.assertTrue(all([p == Piece.EMPTY for p in board.data]))
        for size in range(1, 5):
            board = Board([Piece.CROSS] * (size * size), size)
            self.assertEqual(len(board.data), size * size)
            self.assertTrue(all([p == Piece.CROSS for p in board.data]))

    def test_board_copy(self):
        board = Board([Piece.CROSS] * 9, 3)
        board_copy = board.copy()
        self.assertEqual(len(board.data), len(board_copy.data))
        self.assertTrue(all([p == Piece.CROSS for p in board_copy.data]))

    def test_position_index(self):
        for size in range(1, 5):
            for i in range(0, size * size):
                x, y = Board.index_to_pos(i, size)
                index = Board.pos_to_index(x, y, size)
                self.assertEqual(i, index)

    def test_border_corner(self):
        board = Board(size=3)
        for index in range(0, len(board.data)):
            x, y = board.index_to_pos(index, board.size)
            xborder = board.check_border(x, board.size)
            yborder = board.check_border(y, board.size)
            xcheck = x == 0 or x == board.size - 1
            ycheck = y == 0 or y == board.size - 1
            self.assertEqual(xborder, xcheck)
            self.assertEqual(yborder, ycheck)

    def test_increments(self):
        self.assertListEqual(Board.get_increments(0, 4), [0, 1])
        self.assertListEqual(Board.get_increments(1, 4), [0])
        self.assertListEqual(Board.get_increments(2, 4), [0])
        self.assertListEqual(Board.get_increments(3, 4), [0, -1])

    def test_add_remove(self):
        board = Board()
        for index in range(0, len(board.data)):
            x, y = board.index_to_pos(index, board.size)
            piece = Piece.NOUGHT if index % 2 == 0 else Piece.CROSS
            board.add(piece, x, y)
            self.assertEqual(board.data[index], piece)

        for index in range(0, len(board.data)):
            x, y = board.index_to_pos(index, board.size)
            board.remove(x, y)
            self.assertEqual(board.data[index], Piece.EMPTY)

    def test_empty_coords(self):
        data = [Piece.CROSS] * 9
        board = Board(data, 3)
        for index in range(0, len(board.data)):
            x, y = board.index_to_pos(index, board.size)
            board.data[index] = Piece.EMPTY
            self.assertListEqual(board.get_empty_coords(), [(x, y)])
            board.add(Piece.CROSS, x, y)

if __name__ == "__main__":
    unittest.main()
