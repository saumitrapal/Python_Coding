from turtle import Turtle, Shape, Screen
import turtle
import random

tim = Turtle()
screen = Screen()

turtle.screensize(100, 100)
# tim.hideturtle()

turtle.colormode(255)

direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    
    return color_tuple

for j in range(5):
    for i in range(5):
        tim.color(random_color())
        tim.dot(20)
        tim.penup()
        tim.forward(50)
  
    tim.back(250)
    tim.left(90)
    tim.forward(50)
    tim.dot(20)
    tim.right(90)

    # tim.setheading(random.choice(direction))

screen.exitonclick()