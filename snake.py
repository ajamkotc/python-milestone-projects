from turtle import Turtle


class Snake:
    """Snake class controls the snake.
    
    ...
    
    Methods
    -------
    place_starting():
        Sets up the starting segments
    move_snake():
        Moves the snake forward
    """
    def __init__(self, segment_quantity=3):
        self.segments = [Turtle() for _ in range(segment_quantity)]
        self.place_starting()

    def place_starting(self):
        """Sets up starting snake.

        Sets the color, shape, and starting position of each segment."""

        x_cor = y_cor = 0.0

        for turtle in self.segments:
            turtle.penup()
            turtle.color('white')
            turtle.shape('square')
            turtle.setpos(x=x_cor, y=y_cor)

            x_cor -= 20

    def move_snake(self):
        """Moves the snake forward as a block

        Starting from the end of the snake, segments take the position of the
        next segment, excluding the first one. First one moves forward 20."""

        for turtle_pos in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[turtle_pos - 1].xcor()
            next_y = self.segments[turtle_pos - 1].ycor()
            self.segments[turtle_pos].setpos(x=next_x, y=next_y)

        self.segments[0].forward(20)

    def move_north(self):
        """Points the snake north"""

        self.segments[0].setheading(90)

    def move_west(self):
        """Points the snake west"""

        self.segments[0].setheading(180)

    def move_east(self):
        """Points the snake east"""

        self.segments[0].setheading(0)

    def move_south(self):
        """Points the snake south"""

        self.segments[0].setheading(270)
