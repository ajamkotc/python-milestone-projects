import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('My Snake Game')

new_snake = Snake(3)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.5)
    new_snake.move_snake()

screen.exitonclick()
