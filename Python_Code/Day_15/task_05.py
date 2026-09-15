import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

tultle_color = [
    "CronFlowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "Wheat",
    "Slategray",
    "SeaGreen"
    ]

def draw_shape(number_side):
    angle = (360 // number_side)
    for i in range(number_side):
        tim.forward(100)
        tim.right(angle)
        
for shape in range(3, 11):
    tim.color(random.choice(tultle_color))
    draw_shape(shape)
    
    
screen.exitonclick()