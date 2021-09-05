from tictactoe.board import Piece, Board
from tictactoe.tree import Node

def get_coords(size: int) -> tuple:
    while True:
        try:
            c = input('> ')
            x, y = [int(x) for x in c.split(':')]
            if x in range(1, size + 1) and y in range(1, size + 1):
                return x, y
            else:
                raise Exception
        except:
            print('Invalid coords.')

def generate_all_possible_board_states(node, counter):
    node.winner = node.item.check_winner()
    if node.winner:
        return node.winner.value
    node.addChilds(node.item.all_possible_moves(Piece.NOUGHT if counter % 2 == 0 else Piece.CROSS))
    counter += 1
    node.wsum = 0
    for child in node.childs:
        child.wsum = generate_all_possible_board_states(child, counter)
        node.wsum += child.wsum
    return node.wsum

if __name__ == "__main__":
    board = Board()

    winner = None
    while not winner:
        print(board)
        x, y = get_coords(board.size)
        if not board.add(Piece.CROSS, x - 1, y - 1):
            print('Can\'t place a piece at {}:{}'.format(x, y))
            continue

        root = Node(board)
        generate_all_possible_board_states(root, 0)

        state = None
        for child in root.childs:
            if child.winner == Piece.NOUGHT:
                state = child
                break
            elif not state or child.wsum < state.wsum:
                state = child

        if state:
            board = state.item
            winner = board.check_winner()
        else:
            winner = Piece.EMPTY

    print('-' * 20)
    print(board)
    if winner == Piece.EMPTY:
        print("It's a draw!")
    else:
        print("{} wins!".format(winner.name))

