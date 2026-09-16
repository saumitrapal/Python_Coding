import main
import turtle
import random

tim = turtle.Turtle()
screen = turtle.Screen()

tim.shape("turtle")
tim.hideturtle()

turtle.colormode(255)

for _ in range(10):
    for _ in range(10):
        tim.color(random.choice(main.rgb_color))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.back(500)


screen.exitonclick()