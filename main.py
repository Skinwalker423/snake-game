from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

new_snake = Snake()


def start_game():
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(.1)
        position = new_snake.segments[-1].position()
        position_x = position[0]
        position_y = position[1]
        print(f"position: {position}")
        if position_x > 300 or position_x < -300 or position_y > 300 or position_y < -300:
            is_game_on = False
        else:
            new_snake.move_forward()
    print("Game Over")


screen.listen()
screen.onkeypress(key="s", fun=start_game)
screen.onkey(key="Up", fun=new_snake.up)
screen.onkey(key="Right", fun=new_snake.right)
screen.onkey(key="Left", fun=new_snake.left)
screen.onkey(key="Down", fun=new_snake.down)

screen.exitonclick()
