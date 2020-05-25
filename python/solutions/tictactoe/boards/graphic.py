from pygame.locals import QUIT, MOUSEBUTTONUP
import pygame
import itertools
import sys


class Board:
    """Tic-Tac-Toe Graphic Board.
    
       The board is implemented with pygame and is based on the
       code available at https://github.com/kgodey/pygame-tictactoe.
    """

    # Background color (in rgb)
    BACKGROUND = (255, 255, 255)

    # X lines color 
    X_COLOR = (255, 0, 0)

    # O circles color
    O_COLOR = (0, 0, 255)

    # Separator lines color
    LINE_COLOR = (0, 0, 0)

    # Diaginal Length (for 3x3 board it should be 3)
    DIAG = 3

    # Size of a single board box
    BOX_SIZE = 100

    # The side of the side margins
    MARGIN_SIZE = 20

    # Separator lines width 
    SEPERATOR_LINE_WIDTH = 4

    # Xs and Os line width
    SHAPE_LINE_WIDTH = 5

    # Winner message font
    FONT = 'freesansbold.ttf'

    def __init__(self, values, symbol):
        """Tic-Tac-Toe Board.
            :param values: board values
            :param symbol: starting symbol ('x' or 'o')
        """

        self._symbol = symbol
        self._done = False
        self._values = values


        # Initialize the screen for display
        side_length = Board.DIAG * Board.BOX_SIZE + Board.MARGIN_SIZE * 2 + (Board.SEPERATOR_LINE_WIDTH * (Board.DIAG - 1))
        flags, depth = 0, 32
        self.surface = pygame.display.set_mode((side_length, side_length), flags, depth)

        # Set window title
        pygame.display.set_caption('Tic-Tac-Toe')

        # Fill background color
        self.surface.fill(Board.BACKGROUND)

        # Draw separator lines
        self.draw_lines()

        # Initialize box object which draw Xs and Os
        self.initialize_boxes()

    def draw_lines(self):
        for i in range(1, Board.DIAG):
            start_position = ((Board.BOX_SIZE * i) + (Board.SEPERATOR_LINE_WIDTH * (i - 1))) + Board.MARGIN_SIZE
            width = self.surface.get_width() - (2 * Board.MARGIN_SIZE)
            pygame.draw.rect(self.surface, Board.LINE_COLOR, (start_position, Board.MARGIN_SIZE, Board.SEPERATOR_LINE_WIDTH, width))
            pygame.draw.rect(self.surface, Board.LINE_COLOR, (Board.MARGIN_SIZE, start_position, width, Board.SEPERATOR_LINE_WIDTH))

    def initialize_boxes(self):
        self.boxes = []
        
        top_left_numbers = []
        for i in range(0, Board.DIAG):
            num = ((i * Board.BOX_SIZE) + Board.MARGIN_SIZE + (i * Board.SEPERATOR_LINE_WIDTH))
            top_left_numbers.append(num)
        
        box_coordinates = list(itertools.product(top_left_numbers, repeat=2))
        for i, (x, y) in enumerate(box_coordinates):
            self.boxes.append(Box(x, y, Board.BOX_SIZE, self, i // Board.DIAG, i % Board.DIAG))

    def get_box_at_pixel(self, x, y):
        for index, box in enumerate(self.boxes):
            if box.collidepoint(x, y):
                return box
        return None

    def display_game_over(self, winner):
        surface_size = self.surface.get_height()
        font = pygame.font.Font(Board.FONT, surface_size // 8)
        if winner:
            text = 'Player %s won!' % winner
        else:
            text = 'Draw!'
        text = font.render(text, True, Board.LINE_COLOR, Board.BACKGROUND)
        rect = text.get_rect()
        rect.center = (surface_size // 2, surface_size // 2)
        self.surface.blit(text, rect)

    def wait_for_quit(self, winner=None):
        self.display_game_over(winner)
        clock = pygame.time.Clock()

        # Run event loop
        while not self._done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._done = True

            pygame.display.update()
            clock.tick(30)

        pygame.quit()
        sys.exit()

    def change_symbol(self, symbol):
        self._symbol = symbol.lower()
        
    def next_move(self):
        pygame.init()
        clock = pygame.time.Clock()

        # Run event loop
        while not self._done and ' ' in ''.join(self._values):
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._done = True
                    return
                elif event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    box = self.get_box_at_pixel(x, y)
                    if not box:
                        continue
                    if self._values[box.ij[0]][box.ij[1]] != ' ':
                        continue
                    box.mark(self._symbol)
                    yield box.ij

            pygame.display.update()
            clock.tick(30)

class Box:
    def __init__(self, x, y, size, board, i, j):
        self._size = size
        self._radius = (self._size // 2) - (self._size // 8)
        self._rect = pygame.Rect(x, y, size, size)
        self._board = board
        self._ij = (i, j)

    def mark(self, symbol):
        if symbol == 'x':
            self.mark_x()
        else:
            self.mark_o()

    def collidepoint(self, x, y):
        return self._rect.collidepoint(x, y)

    def mark_x(self):
        pygame.draw.line(self._board.surface, Board.X_COLOR,
                         (self._rect.centerx - self._radius, self._rect.centery - self._radius),
                         (self._rect.centerx + self._radius, self._rect.centery + self._radius),
                         Board.SHAPE_LINE_WIDTH)
        pygame.draw.line(self._board.surface, Board.X_COLOR,
                         (self._rect.centerx - self._radius, self._rect.centery + self._radius),
                         (self._rect.centerx + self._radius, self._rect.centery - self._radius),
                         Board.SHAPE_LINE_WIDTH)
    
    def mark_o(self):
        pygame.draw.circle(self._board.surface, Board.O_COLOR, (self._rect.centerx, self._rect.centery),
                           self._radius, Board.SHAPE_LINE_WIDTH)

    @property
    def ij(self):
        return self._ij
