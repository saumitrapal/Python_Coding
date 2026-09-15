from turtle import Turtle, Screen, Shape
import turtle as t
import random

tim = Turtle()
screen = Screen()

# tim.shape("turtle")
# tim.color("brown2")
tim.hideturtle()
tim.pensize(2)

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

def draw_circle(degree_sheft):
    tim.speed("fastest")
    for i in range(int(360 / degree_sheft)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(degree_sheft)

draw_circle(5)

screen.exitonclick()