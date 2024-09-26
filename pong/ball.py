from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(2)
        self.penup()

    def bounce(self):
        pass

    def wall_collision(self):
        screen = self.getscreen()
        screen_height = screen.window_height() / 2

        return self.distance(x=self.xcor(), y=screen_height) < 20
