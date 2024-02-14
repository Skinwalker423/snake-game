from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)


new_snake = Snake()
new_food = Food()


def start_game():
    is_game_on = True
    score = 0
    while is_game_on:
        screen.update()
        time.sleep(.1)
        distance = new_snake.head.distance(new_food)
        print(f"distance from food is {distance}")
        position = new_snake.head.position()
        position_x = position[0]
        position_y = position[1]
        print(f"position: {position}")
        if distance < 15:
            new_food.move_to_new_location()
            new_snake.add_to_snake()
            score += 1
        if position_x > 300 or position_x < -300 or position_y > 300 or position_y < -300:
            is_game_on = False
        else:
            new_snake.move_forward()
    print("Game Over")
    print(f"Your final score is {score}")


screen.listen()
screen.onkeypress(key="s", fun=start_game)
screen.onkey(key="Up", fun=new_snake.up)
screen.onkey(key="Right", fun=new_snake.right)
screen.onkey(key="Left", fun=new_snake.left)
screen.onkey(key="Down", fun=new_snake.down)

screen.exitonclick()
