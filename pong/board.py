from paddle import Paddle
from turtle import Turtle
from ball import Ball

GAP = 40


class Board:
    """Controls the various items on the game board

    Attributes
    ----------
    left_paddle: Paddle
    right_paddle: Paddle

    Methods
    -------
    position_paddles():
        Positions the two paddles at opposite ends of the screen"""

    def __init__(self):
        self.left_paddle = Paddle()
        self.right_paddle = Paddle()
        self.position_paddles()
        self.draw_divide()
        self.ball = Ball()

    def position_paddles(self):
        """Positions the two paddles at opposite ends of the screen"""

        screen = self.left_paddle.getscreen()
        screen_width = screen.window_width()
        self.left_paddle.setpos(x=-screen_width+GAP, y=0)
        self.right_paddle.setpos(x=screen_width-GAP, y=0)

    def draw_divide(self):
        """Draws the center divide dotted line"""

        # Set up turtle to draw line
        drawer = Turtle()
        drawer.pencolor('white')
        drawer.penup()
        drawer.pensize(20)
        drawer.setheading(90)
        drawer.shape('square')

        # Position turtle at bottom of screen in center
        screen = self.left_paddle.getscreen()
        screen_height = screen.window_height()
        drawer.setpos(x=0, y=-screen_height)

        # Draw until get to top of screen
        while drawer.ycor() < screen_height:
            drawer.pendown()
            drawer.forward(50)
            drawer.penup()
            drawer.forward(50)
