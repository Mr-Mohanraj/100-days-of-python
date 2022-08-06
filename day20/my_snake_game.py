from turtle import Screen
import time
from snake import Snake


screen = Screen()
width = 500
screen = Screen()
screen.bgcolor('black')  # for set background color
screen.setup(width=width, height=width)
screen.tracer(0)  # set animation on the turtle 0 -> off

snake = Snake()
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


is_game_on = True
while is_game_on:
    # redraw the entries Screen
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    snake.coli()

screen.exitonclick()
