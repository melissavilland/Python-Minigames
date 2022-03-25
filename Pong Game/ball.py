from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        # self.dir = 0
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.shape('circle')
        self.color('orchid')
        self.penup()

    # def move(self):
        # if self.ycor() > 280:
        #     self.dir = 1
        # if self.ycor() < -280:
        #     self.dir = 0
        # if self.dir == 0:
        #     new_x = self.xcor() + 5
        #     new_y = self.ycor() + 7
        #     self.goto(new_x, new_y)
        #     time.sleep(0.03)
        # if self.dir == 1:
        #     new_x = self.xcor() + 5
        #     new_y = self.ycor() - 7
        #     self.goto(new_x, new_y)
        #     time.sleep(0.03)

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.move_y *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()




