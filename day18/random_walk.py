import turtle as t
import random

tim = t.Turtle()


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
# for set speed of turtle move."fastest”: 0,“fast”: 10,“normal”: 6,“slow”: 3,“slowest”: 1.
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))# color rgb(r,g,b) or string
    tim.forward(30)
    tim.setheading(random.choice(directions))