import turtle as t
import random

t.colormode(255)
painting_turtle = t.Turtle()
painting_turtle.speed("fastest")
painting_turtle.penup()
#Hide the turtle
painting_turtle.hideturtle()
#Initialize color list
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

painting_turtle.setheading(225)
painting_turtle.forward(300)
painting_turtle.setheading(0)

#Paint 100 randomly colored dots
for num_dots in range(1, 101):
    painting_turtle.dot(20, random.choice(color_list))
    painting_turtle.forward(50)

    if num_dots % 10 == 0:
        #Change direction to start a new row
        painting_turtle.setheading(90)
        painting_turtle.forward(50)
        painting_turtle.setheading(180)
        painting_turtle.forward(500)
        painting_turtle.setheading(0)
