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

class Node:
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
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = BLUE

    def make_path(self):
        self.color = PURPLE

    # draw the cube on the screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append()

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
            spot = Node(i, j, gap, rows)
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
    rows = 50
    grid = make_grid(rows, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            # always check QUIT first
            if event.type == pygame.QUIT:
                run = False

            # cannot create barriers while algorithm runs
            if started:
                continue

            # if we pressed left mouse button, do something
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                # make sure can't override start and end
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            # if we pressed right mouse button, sth else
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:


    pygame.quit()

main(WIN, WIDTH)
