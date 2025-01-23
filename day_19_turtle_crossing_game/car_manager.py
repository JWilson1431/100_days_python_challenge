import time
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self, starting_height):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.setheading(180)
        self.reset_car(starting_y = starting_height)

    def drive_car(self):
        self.forward(10)

    def reset_car(self, starting_y):
        self.goto(x=random.randint(305, 400), y=starting_y)



