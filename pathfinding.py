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

        def get_pos(self):
            return self.row, self.col
