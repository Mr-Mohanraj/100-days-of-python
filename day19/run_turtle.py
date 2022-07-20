import turtle
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bid= screen.textinput(title="Racing", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def create_turtle(x, y, num):
    tom = Turtle(shape='turtle')
    tom.penup()
    tom.goto(x=-x,y=-y)
    tom.color(colors[num])
    all_turtles.append(tom)


def create_coordination():
    x = 230
    y = 100
    for i in range(0, 6):
        create_turtle(x,y,num=i)
        y -= 20

create_coordination()

if user_bid:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bid:
                print(f"You are won! The {winning_turtle} turtle is a winner!")
            else:
                print(f"You are lose! The {winning_turtle} turtle is a winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
