from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.write_score()

    def player1_point(self):
        self.player1_score += 1
        self.clear()
        self.write_score()

    def player2_point(self):
        self.player2_score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.goto(-100, 200)
        self.write(self.player1_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.player2_score, align="center", font=("Courier", 50, "normal"))
