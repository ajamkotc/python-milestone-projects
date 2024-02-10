from turtle import Turtle
import random


def random_pos():
    x_cor = random.randint(a=-200, b=200)
    y_cor = random.randint(a=-200, b=200)

    return x_cor, y_cor


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.setpos(random_pos())
