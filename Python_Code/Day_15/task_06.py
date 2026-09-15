import turtle as t 
import random as ran

tim = t.Turtle()
screen = t.Screen()

tultle_color = [
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    # "Wheat",
    "Slategray",
    "SeaGreen"
    ]

num_list = [0, 90, 180, 270]

tim.shape("turtle")
tim.width(4)
tim.speed(100)
tim.hideturtle()
t.colormode(255)

def random_color():
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    color_tuple = (r, g, b) 
    
    return color_tuple

def random_walk():
    for _ in range(0, 100):
        # tim.color(ran.choice(tultle_color))
        tim.color(random_color())
        tim.forward(100)
        tim.setheading(ran.choice(num_list))
    
random_walk()

# def draw_walk():
#     for i in range(0, 100):
#         tim.color(ran.choice(tultle_color))
#         num = ran.choice(num_list)
#         tim.setx(num)
#         tim.sety(num)
#         tim.speed(num)
    
# draw_walk()



screen.exitonclick()