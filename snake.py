from turtle import Pen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP_DIR = 90
DOWN_DIR = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.list_of_segments = []
        self.create_snake()
        self.head = self.list_of_segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
           self.add_segment(pos)

    def move(self):
        for seg in range(len(self.list_of_segments) - 1, 0, -1):
            new_x = self.list_of_segments[seg - 1].xcor()
            new_y = self.list_of_segments[seg - 1].ycor()
            self.list_of_segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)
    def add_segment(self, pos):
        my_snake = Pen(shape="square")
        my_snake.color("white")
        my_snake.penup()
        my_snake.goto(pos)
        self.list_of_segments.append(my_snake)

    def extend(self):
        self.add_segment(self.list_of_segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN_DIR:
            self.head.setheading(UP_DIR)

    def down(self):
        if self.head.heading() != UP_DIR:
            self.head.setheading(DOWN_DIR)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)