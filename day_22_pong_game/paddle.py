from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_start, y_start):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_start, y_start)

    def move_upwards(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_downwards(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
