from turtle import Turtle

#create tuple to hold starting positions for segments
STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
#Set distance to move by
MOVE_DISTANCE = 20
#Set the directions
LEFT = 0
RIGHT = 180
DOWN = 270
UP= 90

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create segments and append them to list of segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        # Loop through starting with the last number
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(100,1001)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)