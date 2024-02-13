from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create()

    def create(self):
        for index in range(0, 3):
            starting_x = index * -20
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.color("white")
            turtle.goto(x=starting_x, y=0)
            self.segments.insert(0, turtle)
