import unittest

from tictactoe.tree import *
from tictactoe.board import *

class Game(unittest.TestCase):
    TEST_BOARD = [
        Piece.CROSS, Piece.CROSS, Piece.CROSS,
        Piece.CROSS, Piece.NOUGHT, Piece.CROSS,
        Piece.CROSS, Piece.NOUGHT, Piece.NOUGHT
    ]

    TEST_BOARD_2 = [
        Piece.CROSS, Piece.NOUGHT, Piece.CROSS,
        Piece.CROSS, Piece.NOUGHT, Piece.CROSS,
        Piece.NOUGHT, Piece.EMPTY, Piece.EMPTY
    ]

    TEST_BOARD_3 = [
        Piece.CROSS, Piece.NOUGHT, Piece.CROSS,
        Piece.NOUGHT, Piece.CROSS, Piece.NOUGHT,
        Piece.EMPTY, Piece.EMPTY, Piece.EMPTY
    ]

    TEST_BOARD_4 = [
        Piece.NOUGHT, Piece.NOUGHT, Piece.CROSS,
        Piece.NOUGHT, Piece.CROSS, Piece.CROSS,
        Piece.EMPTY, Piece.EMPTY, Piece.EMPTY
    ]

    def test(self):
        board = Board(self.TEST_BOARD_4)
        print(board)
        print(board.get_empty_coords())
        root = Node(board)

        def generate_all_possible_board_states(node, counter):
            if node.item.check_winner():
                return
            node.addChilds(node.item.all_possible_moves(Piece.CROSS if counter % 2 == 0 else Piece.NOUGHT))
            counter += 1
            for child in node.childs:
                generate_all_possible_board_states(child, counter)
        counter = 0
        generate_all_possible_board_states(root, 0)

        root.walk(lambda node, depth: (print(depth), print(node.item), print(node.item.check_winner())))

        def check_winners(node) -> Piece:
            winner = node.item.check_winner()
            if not winner:
                cross = 0
                nought = 0
                for child in node.childs:
                    piece = check_winners(child)
                    if piece == Piece.CROSS:
                        cross += 1
                    elif piece == Piece.NOUGHT:
                        nought += 1
                if cross > nought:
                    winner = Piece.CROSS
                elif nought > cross:
                    winner = Piece.NOUGHT
            return winner

        root.walk(lambda node, depth: (print(depth), print(check_winners(node))))

if __name__ == "__main__":
    unittest.main()
