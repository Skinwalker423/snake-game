from turtle import Screen, Turtle
import time
from snake import Snake

turtles = []

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("green")
screen.title("Snake Game")

new_snake = Snake()

print(new_snake.segments)

for index in range(0, 3):
    starting_x = index * -20
    turtle = Turtle()
    turtle.penup()
    turtle.shape("square")
    turtle.color("white")
    turtle.goto(x=starting_x, y=0)
    turtles.insert(0, turtle)


def move_forward():
    length = len(turtles)
    for i in range(0, length):
        if i < length - 1:
            next_turtle = turtles[i + 1]
            next_turtle_position = next_turtle.position()
            x = next_turtle_position[0]
            y = next_turtle_position[1]
            turtles[i].goto(x, y)

        else:
            turtles[i].forward(20)


def turn_left():
    screen.update()
    time.sleep(.05)
    turtles[-1].left(90)


def turn_right():
    screen.update()
    time.sleep(.05)
    turtles[-1].right(90)


def start_game():
    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(.1)
        position = turtles[-1].position()
        position_x = position[0]
        position_y = position[1]
        print(f"position: {position}")
        if position_x > 300 or position_x < -300 or position_y > 300 or position_y < -300:
            is_game_on = False
        else:

            move_forward()

    print("Game Over")


screen.onkeypress(key="s", fun=start_game)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

screen.listen()
screen.exitonclick()
