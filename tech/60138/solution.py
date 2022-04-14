class Piece:
    def __init__(self, sort, color, position):
        self.sort = sort
        self.color = color
        self.position = position

    def invert_color(self):
        if self.color == "black":
            self.color = "white"
        else:
            self.color = "black"


class Board:
    def __init__(self):
        self.position = {
            (10, 10): Piece("K", "black", (10, 10)),
            (-10, -10): Piece("K", "white", (-10, -10)),
        }
        self.kw = (-10, -10)
        self.kb = (10, 10)

    def add(self, piece):
        if piece.sort == "K" or piece.position in self.position:
            print("invalid query")
        else:
            self.position[piece.position] = piece

    def remove(self, position):
        if position in self.position and self.position[position].sort != "K":
            self.position.pop(position)
        else:
            print("invalid query")

    def move(self, piece, position):
        if piece.position in self.position and self.position[piece.position] == piece:
            if position not in self.position:
                self.position[position] = piece
                del self.position[piece.position]
                piece.position = position
                return
            elif self.position[position].sort != "K" and self.position[position].color != piece.color:
                self.position[position] = piece
                del self.position[piece.position]
                piece.position = position
                return
        print("invalid query")

    def is_mate(self, color):
        if color == "white":
            for i in range(self.kw[0] - 1, self.kw[0] + 2):
                for j in range(self.kw[1] - 1, self.kw[1] + 2):
                    if (i, j) in self.position and self.position[(i, j)].sort != "K" and self.position[(i, j)].color == "black":
                        return True
        elif color == "black":
            for i in range(self.kb[0] - 1, self.kb[0] + 2):
                for j in range(self.kb[1] - 1, self.kb[1] + 2):
                    if (i, j) in self.position and self.position[(i, j)].sort != "K" and self.position[(i, j)].color == "white":
                        return True
        return False
