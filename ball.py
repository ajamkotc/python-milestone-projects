from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(2)
        self.penup()

    def bounce(self):
        screen = self.getscreen()
        screen_height = screen.window_height()
        screen_width = screen.window_width()


