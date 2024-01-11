import pygame
import math
from queue import PriorityQueue
import time

WIDTH = 801
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finder")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Tile:
    def __init__(self, row, col, width, total_rows, total_columns):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def is_path(self):
        return self.color == PURPLE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        # how we handle a comparision using less than operator
        return False


def h(t1, t2):  # h component, estimated distance
    x1, y1 = t1  # tuple unpacking
    x2, y2 = t2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, columns, width):
    grid = []
    tile_width = width // rows
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            tile = Tile(i, j, tile_width, rows, columns)
            tile.draw(WIN)
            grid[i].append(tile)


def draw_grid(win, rows, columns, game_width, game_height):
    grid_gap_row = game_height // rows
    grid_gap_column = game_width // columns
    for i in range(rows + 1):
        pygame.draw.line(
            win, GREY, (0, i * grid_gap_row), (game_width, i * grid_gap_row)
        )
    for j in range(columns + 1):
        pygame.draw.line(
            win, GREY, (j * grid_gap_column, 0), (j * grid_gap_column, game_height)
        )


draw_grid(WIN, 20, 20, 800, 800)
pygame.display.flip()
time.sleep(100)
