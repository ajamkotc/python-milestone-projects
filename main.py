import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('My Snake Game')

starting_turtles = [Turtle() for _ in range(3)]

x_cor = y_cor = 0.0

for turtle in starting_turtles:
    turtle.penup()
    turtle.color('white')
    turtle.shape('square')
    turtle.setpos(x=x_cor, y=y_cor)

    x_cor -= 20

screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(5)

    for turtle_pos in range(len(starting_turtles) - 1, 0, -1):
        next_x = starting_turtles[turtle_pos - 1].xcor()
        next_y = starting_turtles[turtle_pos - 1].ycor()
        starting_turtles[turtle_pos].setpos(x=next_x, y=next_y)

    starting_turtles[0].forward(20)

screen.exitonclick()
