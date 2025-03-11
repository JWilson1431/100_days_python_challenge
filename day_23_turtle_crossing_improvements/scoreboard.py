from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-270, y = 240)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="left",font= FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()