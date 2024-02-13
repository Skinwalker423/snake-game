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

    def move_forward(self):
        length = len(self.segments)
        for i in range(0, length):
            if i < length - 1:
                next_turtle = self.segments[i + 1]
                next_turtle_position = next_turtle.position()
                x = next_turtle_position[0]
                y = next_turtle_position[1]
                self.segments[i].goto(x, y)

            else:
                self.segments[i].forward(20)

    def turn_left(self):
        self.segments[-1].left(90)

    def turn_right(self):
        self.segments[-1].right(90)
