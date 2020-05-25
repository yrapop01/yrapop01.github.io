class Board:
    def __init__(self, values, symbol):
        self.values = values
        self.symbol = symbol

    def print_board(self):
        for row in self.values:
            print(' | '.join(row))
            print('---------')
        print()

    def read_coord(self):
        print('Choose the next coordinate for', self.symbol)
        i = int(input('Next row: '))
        if not (0 <= i <= 2):
            print('Bad coordinate format')
            return None

        j = int(input('Next column: '))
        if not (0 <= j <= 2):
            print('Bad coordinate format')
            return None

        if self.values[i][j] != ' ':
            print('The coordinate is taken.')
            return None
        return (i, j)

    @property
    def symb(self):
        return self.symbol

    def change_symbol(self, symbol):
        self.symbol = symbol

    def next_move(self):
        while ' ' in ''.join(self.values):
            self.print_board()
            coord = self.read_coord()
            while coord is None:
                coord = self.read_coord()
            yield coord

    def wait_for_quit(self, winner):
        print(winner, 'wins')
        self.print_board()
