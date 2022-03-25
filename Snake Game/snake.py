from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(self.snake_body[-1].position())

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)
