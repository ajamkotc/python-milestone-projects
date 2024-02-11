import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

WIDTH = 600
HEIGHT = 600

# Set up the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.bgcolor('black')
screen.title('My Snake Game')

# Create instances of game objects
new_snake = Snake(3)
food = Food()
scoreboard = ScoreBoard()

# Set up key bindings
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
    scoreboard.display_score()
    screen.update()
    time.sleep(0.1)
    new_snake.move_snake()

    # Check if collision with food
    if new_snake.segments[0].distance(food) < 20:
        food.refresh()
        new_snake.add_segment()
        scoreboard.add_point()

    # Check if collision with wall
    if new_snake.wall_collision():
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
