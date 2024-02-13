from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("green")
screen.title("Snake Game")

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


screen.onkeypress(key="s", fun=start_game)
screen.onkey(key="a", fun=new_snake.turn_left)
screen.onkey(key="d", fun=new_snake.turn_right)

screen.listen()
screen.exitonclick()
