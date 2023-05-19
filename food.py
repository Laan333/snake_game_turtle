from turtle import Pen
from random import randint

class Food(Pen):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("purple")
        self.speed("fastest")



    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))