from turtle import Turtle
import random


def random_location():
    x = random.randint(a=-280, b=280)
    y = random.randint(a=-280, b=280)
    coordinates = (x, y)
    return coordinates


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.resizemode()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed(10)
        self.goto(random_location())

    def move_to_new_location(self):
        self.goto(random_location())
