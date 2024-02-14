from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)
screen.title("Snake Game")
screen.textinput(title="Snake Game", prompt="Press any key to start")

scoreboard = Scoreboard()
new_snake = Snake()
new_food = Food()




def start_game():
    is_game_on = True
    score = 0
    while is_game_on:
        screen.update()
        time.sleep(.1)
        distance = new_snake.head.distance(new_food)

        position = new_snake.head.position()
        position_x = position[0]
        position_y = position[1]

        if distance < 15:
            new_food.move_to_new_location()
            new_snake.add_to_snake()
            scoreboard.increase_score()

        if position_x > 280 or position_x < -280 or position_y > 280 or position_y < -280 or new_snake.has_collided():
            is_game_on = False
        else:
            new_snake.move_forward()
    print("Game Over")
    print(f"Your final score is {scoreboard.score}")
    scoreboard.game_over()


screen.listen()

screen.onkey(key="Up", fun=new_snake.up)
screen.onkey(key="Right", fun=new_snake.right)
screen.onkey(key="Left", fun=new_snake.left)
screen.onkey(key="Down", fun=new_snake.down)

start_game()

screen.exitonclick()
