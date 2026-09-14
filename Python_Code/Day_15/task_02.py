from turtle import Turtle, Shape, Screen

timmy_the_turtle = Turtle()
screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("brown2")


for i in range(0, 4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)




screen.exitonclick()