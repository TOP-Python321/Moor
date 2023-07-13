class ChessKing:
    files = {chr(ord('a') + i): i + 1 for i in range(8)}
    ranks = {str(i): i for i in range(1, 9)}

    def __init__(self, color: str = 'white', square: str = None):
        self.color = color
        if square is None:
            if color == 'white':
                self.square = 'e1'
            if color == 'black':
                self.square = 'e8'
        else:
            self.square = square

    def __repr__(self):
        return f'\'{self.color[0].upper()}K: {self.square}\''

    def __str__(self):
        return f'{self.color[0].upper()}K: {self.square}'

    def is_turn_valid(self, new_square: str) -> bool:
        """
        Проверяет, возможен ли для данной фигуры ход с текущего поля на новое.
        :param new_square: строка нового поля.
        :return: bool
        """
        file = new_square[0]
        rank = new_square[1]
        if (abs(self.files[self.square[0]] - self.files[file]) <= 1
                and abs(self.ranks[self.square[1]] - self.ranks[rank]) <= 1):
            return True

    def turn(self, new_square: str) -> None:
        """
        Выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход.
        :param new_square: строка нового поля.
        """
        if not self.is_turn_valid(new_square):
            raise ValueError
        else:
            self.square = new_square



# >>> wk = ChessKing()
# >>> wk.color
# >>> 'white'
# >>> wk.square
# >>> 'e1'
# >>> wk.turn('e2')
# >>> bk = ChessKing('black')
# >>> print(bk)
# >>> BK: e8
# >>> bk.turn('d3')
# >>> ValueError
