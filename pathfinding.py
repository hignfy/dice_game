import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH)) # screen
pygame.display.set_caption("Path Finder") # screen's name

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
ORANGE = (255, 165, 0)
PURPLE = (128,0,128)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        # position determined by multiplying row number by cube width
        self.x = row * width
        self.y = col * width
        # all cubes start white
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

        # get the current position
        def get_pos(self):
            return self.row, self.col

        # how to see visually that a cube has been checked
        def is_closed(self):
            self.color == RED

        # how to see that a cube is currently being checked
        def is_open(self):
            self.color == GREEN

        # what's a barrier?
        def is_barrier(self):
            return self.color == BLACK

        def is_start(self):
            return self.color == ORANGE

        def is_end(self):
            return self.color == BLUE

        def reset(self):
            self.color == WHITE

        def make_closed(self):
            self.color == RED

        def make_open(self):
            self.color == GREEN

        def make_barrier(self):
            self.color == BLACK

        def make_end(self):
            self.color == BLUE

        def make_path(self):
            self.color == PURPLE

        # draw the cube on the screen
        def draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        def update_neighbors(self, grid):
            pass

        # lt is less than function
        def __lt__(self, other):
            return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# 2D array
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot) # lists inside lists that store spots

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

# paint over everything on the canvas and replace with update
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    