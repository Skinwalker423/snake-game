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

    def add_to_snake(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")

        tail_position = self.segments[0].position()
        heading = self.get_heading()
        x = tail_position[0]
        y = tail_position[1]

        if heading == 180:
            x += 20
        elif heading == 90:
            y -= 20
        elif heading == 270:
            y += 20
        else:
            x -= 20
        turtle.goto(x, y)
        self.segments.insert(0, turtle)

    def has_collided(self):
        if len(self.segments) < 4:
            return False

        for square in self.segments[:-4]:
            space_between_tail = self.head.distance(square)
            if space_between_tail < 5:
                print(f"has collided. distance is {space_between_tail}")
                return True

        return False
