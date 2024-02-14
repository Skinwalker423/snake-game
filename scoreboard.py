from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.increase_score()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=True, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.speed(10)
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=True, align=ALIGN, font=FONT)