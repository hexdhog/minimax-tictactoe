from enum import Enum

class Piece(Enum):
    EMPTY = 0
    CROSS = 1
    NOUGHT = -1

    def __str__(self):
        if self.value == Piece.EMPTY.value:
            return ' '
        elif self.value == Piece.CROSS.value:
            return 'X'
        elif self.value == Piece.NOUGHT.value:
            return 'O'
        else:
            return ''

class Board:
    DEFAULT_SIZE = 3

    def __init__(self, data: list = None, size: int = DEFAULT_SIZE):
        if data and len(data) / size == size:
            self.size = size
            self.data = data
        else:
            self.size = size
            self.data = [Piece.EMPTY] * (self.size ** 2)

    def __str__(self):
        res = ''
        board_str = '|{}|{}|{}|'
        for i in range(0, len(self.data), self.size):
            s = board_str.format(*self.data[i:i + self.size])
            if i == 0:
                res += '-' * len(s) + '\n'
            res += s + '\n'
            res += '-' * len(s) + '\n'
        return res

    def copy(self):
        return Board(self.data.copy(), self.size)

    @classmethod
    def pos_to_index(cls, xpos: int, ypos: int, size: int):
        return (ypos * size) + xpos

    @classmethod
    def index_to_pos(cls, index: int, size: int) -> tuple:
        return (int(index % size), int(index / size))

    @classmethod
    def check_border(cls, pos: int, size: int) -> bool:
        return pos == 0 or pos == size - 1

    @classmethod
    def check_corner(cls, x: int, y: int, size: int) -> bool:
        return cls.check_border(x, size) and cls.check_border(y, size)

    @classmethod
    def get_increments(cls, pos: int, size: int) -> list:
        incs = [0]
        if pos == 0:
            incs.append(1)
        elif pos == size - 1:
            incs.append(-1)
        return incs

    def add(self, piece: Piece, xpos: int, ypos: int) -> bool:
        index = self.pos_to_index(xpos, ypos, self.size)
        if index < len(self.data) and self.data[index] == Piece.EMPTY:
            self.data[index] = piece
            return True
        else:
            return False

    def remove(self, xpos: int, ypos: int):
        index = self.pos_to_index(xpos, ypos, self.size)
        if index < len(self.data):
            self.data[index] = Piece.EMPTY

    def get_empty_coords(self) -> list:
        coords = []
        for i in range(len(self.data)):
            piece = self.data[i]
            if piece == Piece.EMPTY:
                coords.append(self.index_to_pos(i, self.size))
        return coords

    def all_possible_moves(self, piece: Piece) -> list:
        empty_coords = self.get_empty_coords()
        boards = []
        for x, y in empty_coords:
            b = self.copy()
            b.add(piece, x, y)
            boards.append(b)
        return boards

    def check_line(self, piece: Piece, xpos: int, ypos: int, xinc: int, yinc: int) -> bool:
        if xinc == 0 and yinc == 0:
            return False
        data = []
        while xpos in range(0, self.size) and ypos in range(0, self.size):
            index = self.pos_to_index(xpos, ypos, self.size)
            if self.data[index] == piece:
                data.append(self.data[index])
            xpos += xinc
            ypos += yinc
        return len(data) == self.size

    def check_winner(self, pieces: list = [Piece.CROSS, Piece.NOUGHT]) -> Piece:
        for x in range(0, self.size):
            xincs = self.get_increments(x, self.size)
            for y in range(0, self.size):
                yincs = self.get_increments(y, self.size)
                for xinc in xincs:
                    for yinc in yincs:
                        for piece in pieces:
                            if self.check_line(piece, x, y, xinc, yinc):
                                return piece
        return None
