# SETTINGS #

# IMPORTS #
from tkinter import *
import random
from tkinter import messagebox
import pygame as pg

# CONSTANT VARIABLES #
TITLE = "SNAKE"
SNAKECOLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"
FPS = 200  # Game Speed
HEIGHT = 800  # Window Height
WIDTH = 800  # Window Width
geoString = str(WIDTH)+'x'+str(HEIGHT)  # String containing height and width to build the interface.
TILE_SIZE = 50  # Size of each tile on the board

# DEFINING CONTROLS AND SOUNDS #
sounds = ["assets/sounds/music.ogg", "assets/sounds/death.wav", "assets/sounds/apple.wav"]
binds = ["<Left>", "<Right>", "<Up>", "<Down>", "<a>", "<d>", "<w>", "<s>"]
dirs = ["left", "right", "up", "down", "left", "right", "up", "down"]

# VARYING #
BODY_PARTS = 3



