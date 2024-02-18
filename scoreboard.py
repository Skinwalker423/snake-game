from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.create_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=True, align=ALIGN, font=FONT)

    def create_scoreboard(self):
        self.speed(10)
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.create_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=True, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.create_scoreboard()

