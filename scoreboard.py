from turtle import Turtle


class ScoreBoard(Turtle):
    """Represents the game score.

    Methods
    -------
    add_point():
        Adds a point to the current score
    display_score():
        Clears the previous score and displays an updated one
    game_over():
        Prints the words 'Game Over' in the middle of the screen"""
    def __init__(self):
        super().__init__()
        current_screen = self.getscreen()
        self.score = 0
        self.setpos(0, (current_screen.window_height()/2)-20)
        self.color('red')
        self.hideturtle()

    def add_point(self):
        """Adds a point to the current score"""

        self.score += 1

    def display_score(self):
        """Clears the previous score and displays an updated one"""

        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 12, 'normal'))

    def game_over(self):
        """Prints the words 'Game Over' in the middle of the screen"""

        self.home()
        self.write("Game Over", align='center', font=('Arial', 12, 'bold'))
