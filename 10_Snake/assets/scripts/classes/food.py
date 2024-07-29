# FOOD OBJECT #

# _IMPORTS_ #
from assets.scripts.settings import *


class Food(object):
    def __init__(self, game):
        self.game = game  # Defines game as an object in the current function, allowing access to variables and functions in the game class.
        # PLACING FOOD #
        x = random.randint(0, (WIDTH-TILE_SIZE)/TILE_SIZE-1)*TILE_SIZE
        y = random.randint(0, (HEIGHT-TILE_SIZE)/TILE_SIZE-1)*TILE_SIZE

        self.coords = [x,y]
        self.game.canvas.create_oval(x,y,
                                     x+TILE_SIZE,
                                     y+TILE_SIZE,
                                     fill=FOOD_COLOR,
                                     tag="food")
