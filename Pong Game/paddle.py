from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y_coord = self.ycor()
        self.sety(y_coord + 40)

    def go_down(self):
        y_coord = self.ycor()
        self.sety(y_coord - 40)
