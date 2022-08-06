from turtle import Turtle, Screen
"""IN Turtle 0 , 90, 180 and 270 are degree of position"""
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # for coordination of the turtle(head body part)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_part = []
        self.create_snake()
        self.head = self.snake_part[0]
        self.position_x = 0
        self.position_y = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

        
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_part.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_part[-1].position())

    def move(self):
        for num in range(len(self.snake_part) - 1, 0, -1):
            x = self.snake_part[num - 1].xcor()
            y = self.snake_part[num - 1].ycor()
            self.snake_part[num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
        self.position_x = self.head.pos()[0]
        self.position_y = self.head.pos()[1]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

#  for stop game over hit the wall 
    # def coli(self):
    #     if self.position_x > 480:
    #         self.head.goto(-250, self.position_y)
    #     elif self.position_x < -480:
    #         self.head.goto(250, self.position_y)
    #     elif self.position_y > 480:
    #         self.head.goto(self.position_x, -250)
    #     elif self.position_y < -480:
    #         self.head.goto(self.position_x, 250)