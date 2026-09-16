from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=400, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle is gonna win the race, Enter the color of turtle : ")

is_race_on = False
turtle_color = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(f"You've won! The {winning_color} turtle is the winner!")
            else:
                screen.title(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()