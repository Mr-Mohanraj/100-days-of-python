import turtle as t

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup() # penup means pen do not touch the screen
    tim.forward(10)
    tim.pendown()# pendown opposite of the penup