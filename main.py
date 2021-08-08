from turtle import Screen
from food import Food
from snake import Snake
from score import Scoreboard
import time

screen = Screen()
screen.title('Snake Game')
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor('black')

game_running = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')

# score = 0

while game_running:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_score()
        snake.extend()
        food.refresh()

    # collision with body
    for pos in snake.squares[1:]:
        if snake.head.distance(pos) < 15:
            # game_running = False
            scoreboard.reset()
            snake.reset()

    # game_running = False

screen.exitonclick()
