from pygame.locals import QUIT, MOUSEBUTTONUP
import pygame
import itertools
import sys

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

class Board:
    def __init__(self, values, symbol, grid_size=3, box_size=200, border=20, line_width=5):
        self.symbol = symbol
        self._done = False
        self.values = values

        self.grid_size = grid_size
        self.box_size = box_size
        self.border = border
        self.line_width = line_width
        surface_size = (self.grid_size * self.box_size) + (self.border * 2) + (self.line_width * (self.grid_size - 1))
        self.surface = pygame.display.set_mode((surface_size, surface_size), 0, 32)

        pygame.display.set_caption('Tic Tac Toe')
        self.surface.fill(WHITE)
        self.draw_lines()
        self.initialize_boxes()

    def draw_lines(self):
        for i in range(1, self.grid_size):
            start_position = ((self.box_size * i) + (self.line_width * (i - 1))) + self.border
            width = self.surface.get_width() - (2 * self.border)
            pygame.draw.rect(self.surface, BLACK, (start_position, self.border, self.line_width, width))
            pygame.draw.rect(self.surface, BLACK, (self.border, start_position, width, self.line_width))

    def initialize_boxes(self):
        self.boxes = []
        
        top_left_numbers = []
        for i in range(0, self.grid_size):
            num = ((i * self.box_size) + self.border + (i * self.line_width))
            top_left_numbers.append(num)
        
        box_coordinates = list(itertools.product(top_left_numbers, repeat=2))
        for i, (x, y) in enumerate(box_coordinates):
            self.boxes.append(Box(x, y, self.box_size, self, i // self.grid_size, i % self.grid_size))

    def get_box_at_pixel(self, x, y):
        for index, box in enumerate(self.boxes):
            if box.rect.collidepoint(x, y):
                return box
        return None

    def display_game_over(self, winner):
        surface_size = self.surface.get_height()
        font = pygame.font.Font('freesansbold.ttf', surface_size // 8)
        if winner:
            text = 'Player %s won!' % winner
        else:
            text = 'Draw!'
        text = font.render(text, True, BLACK, WHITE)
        rect = text.get_rect()
        rect.center = (surface_size // 2, surface_size // 2)
        self.surface.blit(text, rect)

    def wait_for_quit(self, winner=None):
        self.display_game_over(winner)
        clock = pygame.time.Clock()

        while not self._done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._done = True

            pygame.display.update()
            clock.tick(30)

        pygame.quit()
        sys.exit()

    def change_symbol(self, symbol):
        self.symbol = symbol
        
    def next_move(self):
        pygame.init()
        clock = pygame.time.Clock()

        while not self._done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._done = True
                    return
                elif event.type == MOUSEBUTTONUP:
                    x, y = event.pos
                    box = self.get_box_at_pixel(x, y)
                    if not box:
                        continue
                    if self.values[box.ij[0]][box.ij[1]] != ' ':
                        continue
                    if self.symbol.lower() == 'x':
                        box.mark_x()
                    else:
                        box.mark_o()
                    yield box.ij

            pygame.display.update()
            clock.tick(30)

class Box:
    def __init__(self, x, y, size, board, i, j):
        self.size = size
        self.line_width = int(self.size / 40) if self.size > 40 else 1
        self.radius = (self.size // 2) - (self.size // 8)
        self.rect = pygame.Rect(x, y, size, size)
        self.board = board
        self.ij = (i, j)
    
    def mark_x(self):
        pygame.draw.line(self.board.surface, RED, (self.rect.centerx - self.radius, self.rect.centery - self.radius), (self.rect.centerx + self.radius, self.rect.centery + self.radius), self.line_width)
        pygame.draw.line(self.board.surface, RED, (self.rect.centerx - self.radius, self.rect.centery + self.radius), (self.rect.centerx + self.radius, self.rect.centery - self.radius), self.line_width)
    
    def mark_o(self):
        pygame.draw.circle(self.board.surface, BLUE, (self.rect.centerx, self.rect.centery), self.radius, self.line_width)
