import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('My Snake Game')

new_snake = Snake(3)
food = Food()

screen.onkey(new_snake.move_east, key='d')
screen.onkey(new_snake.move_west, key='a')
screen.onkey(new_snake.move_north, key='w')
screen.onkey(new_snake.move_south, key='s')
screen.onkey(new_snake.move_east, key='Right')
screen.onkey(new_snake.move_west, key='Left')
screen.onkey(new_snake.move_north, key='Up')
screen.onkey(new_snake.move_south, key='Down')
screen.listen()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    new_snake.move_snake()

    if new_snake.segments[0].distance(food) < 20:
        food.refresh()
        new_snake.add_segment()

screen.exitonclick()
