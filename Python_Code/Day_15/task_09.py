import turtle, random

tim = turtle.Turtle()
screen = turtle.Screen()

turtle.colormode(255)
radius_list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    
    return color_tuple

for i in radius_list:
    tim.color(random_color())
    tim.circle(i)
    tim.left(90)
    tim.penup()
    tim.forward(10)
    tim.right(90)
    tim.pendown()



screen.exitonclick()