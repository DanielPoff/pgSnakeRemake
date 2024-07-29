# GAME OBJECT #

# _IMPORTS_ #
from assets.scripts.settings import *
from assets.scripts.classes.food import Food
from assets.scripts.classes.snake import Snake


# GAME OBJECT #
class Game(object):
    def __init__(self):
        self.root = Tk()
        # OBJECTS #
        self.snake, self.food = None, None
        # SOUNDS #
        self.death_snd, self.eat_snd = None, None
        self.header, self.canvas = None, None
        self.score = 0
        self.dir = random.choice(["down", "right"])
        # FUNCTIONS #
        self.root_setup()  #  Setup window and bind controls
        self.create_widgets()  # Build widgets on the screen
        self.load_sounds()  # Binds sounds to functions
        self.setup_game()  # Starts gameloop and sets game to the start for the player

    def play(self):
        self.root.mainloop()

    def setup_game(self):
        # Set up game objects and values and starts game loop #
        self.canvas.delete(ALL)
        self.snake = Snake(self)
        self.food = Food(self)
        self.score = 0
        self.dir = "down"
        # Using f"Score: {self.score}" is the same as "Score: {}".format(self.score)
        self.header.config(text=f"Score: {self.score}")
        pg.mixer.music.play(-1)
        self.root.after(500, self.tick)

    def root_setup(self):
        # _BUILDING WINDOW_
        self.root.resizable(False, False)
        self.root.geometry(geoString)
        self.root.title(TITLE)
        self.root.config(bg=BG_COLOR)
        self.root.iconbitmap("assets/sprites/snake.ico")
        # _CONTROLS_
        direction = 0
        # for item in dirs:
        #     print(item)
        # self.root.bind(binds[len(item)], lambda event:self.change_dir(item))
        self.root.bind(binds[0], lambda event: self.change_dir(dirs[0]))
        self.root.bind(binds[1], lambda event: self.change_dir(dirs[1]))
        self.root.bind(binds[2], lambda event: self.change_dir(dirs[2]))
        self.root.bind(binds[3], lambda event: self.change_dir(dirs[3]))
        self.root.bind(binds[4], lambda event: self.change_dir(dirs[0]))
        self.root.bind(binds[5], lambda event: self.change_dir(dirs[1]))
        self.root.bind(binds[6], lambda event: self.change_dir(dirs[2]))
        self.root.bind(binds[7], lambda event: self.change_dir(dirs[3]))

    def tick(self):  # Detects where the snake is and preforms collision checks,
        x, y = self.snake.coords[0]
        # Moving the snake
        if self.dir == dirs[2]:
            y -= TILE_SIZE
        elif self.dir == dirs[3]:
            y += TILE_SIZE
        elif self.dir == dirs[0]:
            x -= TILE_SIZE
        elif self.dir == dirs[1]:
            x += TILE_SIZE
        self.snake.coords.insert(0,(x,y))
        square = self.canvas.create_rectangle(x,y,x+TILE_SIZE,y+TILE_SIZE,fill=SNAKECOLOR)
        self.snake.squares.insert(0, square)

        # CHECKING FOR COLLISION BETWEEN SNAKE AND FOOD
        if x == self.food.coords[0] and y == self.food.coords[1]:
            self.score += 1
            self.eat_snd.play()
            self.header.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(self)
        else:
            # Delete last part of snake as it moves
            del self.snake.coords[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]
        # Collision with snake and body or walls and head
        if self.check_collisions():
            self.game_over()
            return

        # Making sure food is obtainable
        if self.food.coords[1] < 0 or self.food.coords[0] > WIDTH:
            self.canvas.delete("food")
            self.food = Food(self)
        if self.food.coords[1] < 0 or self.food.coords[1] > HEIGHT:
            self.canvas.delete("food")
            self.food = Food(self)

        # del self.snake.coords[-1]
        # self.canvas.delete(self.snake.squares[-1])
        # del self.snake.squares[-1]

        self.root.after(FPS, self.tick)

    def check_collisions(self):
        # Check to see if snake hits an object or barrier
        x, y = self.snake.coords[0]
        if (x < 0 or x > WIDTH) or (y < 0 or y > HEIGHT):
            return True
        for part in self.snake.coords[1:]:
            if x == part[0] and y == part[1]:
                return True

    def change_dir(self, direction):  # Changes the direction the snake is moving when a specific keypress is detected.
        if direction == "left":
            if self.dir != "right":
                self.dir = direction
        elif direction == "right":
            if self.dir != "left":
                self.dir = direction
        elif direction == "up":
            if self.dir != "down":
                self.dir = direction
        elif direction == "down":
            if self.dir != "up":
                self.dir = direction
        print(self.dir)

    def create_widgets(self):  # Sets up canvas
        self.header = Label(self.root, bg=BG_COLOR, fg="#FFFFFF", text=f"Score: {self.score}", font="consolas 40 bold")
        self.canvas = Canvas(self.root, bg=BG_COLOR, width=WIDTH, height=HEIGHT)

        self.header.pack(side=TOP)
        self.canvas.pack()

    def load_sounds(self):
        # Method will be called to load in all sounds. #
        pg.mixer.init()
        pg.mixer.music.load(sounds[0])
        pg.mixer.music.set_volume(.3)
        self.death_snd = pg.mixer.Sound(sounds[1])
        self.eat_snd = pg.mixer.Sound(sounds[2])

    def game_over(self):  # Game over title screen. Stops game entirely and give the player the option to play again.
        print("GAME OVER")
        pg.mixer.music.fadeout(1500)
        self.death_snd.play()
        self.canvas.delete(ALL)
        self.canvas.create_text(WIDTH/2, HEIGHT/2, font="consolas 60 bold", text=f"!!!GAME OVER!!!\nScore: {self.score}",
                                fill="red", tag="gameover")
        answer = messagebox.askyesno("Game Over", "Would you like to play again?")
        if answer:
            self.root.after(500, self.setup_game)
        else:
            self.root.after(500, self.root.destroy)





