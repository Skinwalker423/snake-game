from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[-1]

    def create(self):
        for position in STARTING_POSITIONS:
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.color("white")
            turtle.goto(position)
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
                self.segments[i].forward(MOVE_DISTANCE)

    def up(self):
        direction = self.get_heading()
        if direction == 270:
            return
        self.head.setheading(90)

    def right(self):
        direction = self.get_heading()
        if direction == 180:
            return
        self.head.setheading(0)

    def left(self):
        direction = self.get_heading()
        if direction == 0:
            return
        self.head.setheading(180)

    def down(self):
        direction = self.get_heading()
        if direction == 90:
            return
        self.head.setheading(270)

    def get_heading(self):
        if not self.head:
            return 0
        else:
            return self.head.heading()
