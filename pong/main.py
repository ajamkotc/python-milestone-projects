import time
from turtle import Screen
from board import Board
import pyautogui

# Get the size of the display monitor
WIDTH = pyautogui.size()[0]
HEIGHT = pyautogui.size()[1]

# Initialize the screen and set it to refresh manually
screen = Screen()
screen.tracer(0)

# Initialize the game board to display items
board = Board()

# Set up screen based on the size of the monitor
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')

# Set up key bindings
screen.onkey(fun=board.left_paddle.move_north, key='w')
screen.onkey(fun=board.left_paddle.move_south, key='s')
screen.listen()

# Run game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(1)
    board.ball.setheading(90)
    board.ball.forward(50)
    board.ball.wall_collision()


screen.exitonclick()
