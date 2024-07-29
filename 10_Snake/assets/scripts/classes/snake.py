# SNAKE OBJECT #

# _IMPORTS_ #
from assets.scripts.settings import *


class Snake(object):
    def __init__(self, game):
        self.game = game  # Defines game as an object in the current function, allowing access to variables and functions in the game class.
        self.body_size = BODY_PARTS
        self.coords = []  # Creates a list for the positions of the body sections.
        self.squares = []  # Creates a list of the tiles

        for i in range(self.body_size):
            self.coords.append([0, 0])
        for x,y in self.coords:
            square = self.game.canvas.create_rectangle(x, y,
                                                       x+TILE_SIZE,
                                                       y+TILE_SIZE,
                                                       fill=SNAKECOLOR)
            self.squares.append(square)
