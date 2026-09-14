from turtle import Turtle, Shape, Screen

tim = Turtle()
screen = Screen()


tim.shape("turtle")
tim.color("brown2")


for i in range(0, 15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()




screen.exitonclick()