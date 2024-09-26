from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.setpos(self.random_pos())

    def random_pos(self):
        current_screen = self.getscreen()
        screen_height = int(current_screen.window_height() / 2) - 20
        screen_width = int(current_screen.window_width() / 2) - 20
        x_cor = random.randrange(start=-screen_width, stop=screen_width, step=10)
        y_cor = random.randrange(start=-screen_height, stop=screen_height, step=10)

        return x_cor, y_cor
