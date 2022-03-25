from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


PADDLE_POSITIONS = [(-350, 0), (350, 0)]

screen = Screen()
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
player1 = Paddle(PADDLE_POSITIONS[0])
player2 = Paddle(PADDLE_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()
screen.onkey(fun=player1.go_up, key='w')
screen.onkey(fun=player1.go_down, key='s')

screen.onkey(fun=player2.go_up, key='Up')
screen.onkey(fun=player2.go_down, key='Down')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(player2) < 50 and ball.xcor() > 320) or (ball.distance(player1) < 50 and ball.xcor()) < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player1_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player2_point()

screen.exitonclick()
