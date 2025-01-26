import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

#Set up screen for the snake game
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

#update the screen now that the snake was created
screen.update()
play_game = True

while play_game:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #check if food and snake collide
    if snake.head.distance(food) < 15:
        #food was eaten, move it to a new random location and increment score
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    #detect head/tail collision
    for segment in snake.segments[1:]:
        #do not compare snake head to itself
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()