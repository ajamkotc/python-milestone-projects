from turtle import Turtle


class Snake:
    """Snake class controls the snake.
    
    ...
    
    Methods
    -------
    place_starting():
        Sets up starting snake
    move_snake():
        Moves the snake forward as a block
    add_segment():
        Adds a new segment to the snake
    move_north():
        Points the snake north
    move_south():
        Points the snake south
    move_east():
        Points the snake east
    move_west():
        Points the snake west
    """
    def __init__(self, segment_quantity=3):
        self.segments = [Turtle() for _ in range(segment_quantity)]
        self.place_starting()

    def add_segment(self):
        """Adds a new segment to the snake"""

        last_segment = self.segments[-1]
        last_pos = last_segment.pos()
        last_x = last_pos[0]
        last_y = last_pos[1]

        new_segment = Turtle()
        new_segment.penup()
        new_segment.color('white')
        new_segment.shape('square')
        new_segment.setpos(last_x, last_y)
        self.segments.append(new_segment)

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

    def wall_collision(self):
        current_screen = self.segments[0].getscreen()
        screen_height = current_screen.window_height()
        screen_width = current_screen.window_width()

        snake_x = abs(self.segments[0].xcor())
        snake_y = abs(self.segments[0].ycor())

        if snake_x > (screen_width/2 - 10) or snake_y > (screen_height/2 - 10):
            return True
        else:
            return False

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

        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def move_west(self):
        """Points the snake west"""
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def move_east(self):
        """Points the snake east"""

        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)

    def move_south(self):
        """Points the snake south"""

        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)
