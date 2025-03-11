from turtle import Screen
from player import Player
from car_manager import CarManager
import random
import time
from scoreboard import Scoreboard


SCREEN_DELAY = 0.1
#Create list of delays to use to ensure cars start at different times
DELAYS = [0, 2000, 6000, 9000, 14000, 19000, 22000, 24000, 45000, 69000, 78000, 100000]

#create list of possible starting y locations
starting_heights = []
for i in range(-250, 250, 20):
    starting_heights.append(i)

#set up screen
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

#initialize turtle
turtle = Player()

#initialize scoreboard
scoreboard = Scoreboard()

#initialize list of cars and create the cars
cars = []
for i in range (1,11):
    car = CarManager(starting_height=random.choice(starting_heights))
    cars.append(car)

screen.listen()
screen.onkey(turtle.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(SCREEN_DELAY)
    screen.update()
    for car in cars:
        if turtle.distance(car) < 20:
            turtle.go_to_start()
            scoreboard.reset_score()
            SCREEN_DELAY = 0.1
        if turtle.ycor() >=280:
            scoreboard.increment_score()
            turtle.go_to_start()
            SCREEN_DELAY *= 0.9
        if car.xcor() > -320:
            screen.ontimer(car.drive_car, random.choice(DELAYS))
        else:
            car.reset_car(random.choice(starting_heights))

screen.exitonclick()
