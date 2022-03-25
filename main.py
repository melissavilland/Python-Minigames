from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.tracer(0)
screen.bgcolor('black')
snake_body = []
# x, y = 0, 0
# for _ in range(3):
#     new_turtle = Turtle(shape='square')
#     new_turtle.color('white')
#     new_turtle.penup()
#     new_turtle.goto(x=x, y=y)
#     x -= 20
#     snake_body.append(new_turtle)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
k = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290 or snake.head.xcor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
