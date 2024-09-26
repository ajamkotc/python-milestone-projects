from turtle import Turtle

SPEED = 10


class Paddle(Turtle):
    """Represents a paddle on the board

    Methods
    -------
    move_north():
        Moves the paddle upwards
    move_south():
        Moves the paddle downwards"""

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape('square')
        self.penup()
        self.shapesize(1, 5)
        self.speed(0)
        self.color('white')

    def move_north(self):
        """Moves the paddle upwards"""

        self.setheading(90)

        screen = self.getscreen()
        height = screen.window_height() / 2

        if self.distance(x=self.xcor(), y=height) > 60:
            self.forward(SPEED)

    def move_south(self):
        """Moves the paddle downwards"""

        self.setheading(270)
        self.forward(SPEED)
