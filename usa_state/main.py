import turtle, pandas
from turtle import Turtle, Screen


ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

screen = Screen()
screen.title("U.S State Turtle Game")
tim = Turtle()
turtle.bgpic("blank_states_img.gif")
# screen.addshape("blank_states_img.gif")
# tim.shape("blank_states_img.gif")





data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()

# print(all_state)
gauss_state = []

while len(gauss_state) < 50:
    user_gauss = turtle.textinput(title=f"{len(gauss_state)}/50 State correct", 
                                  prompt="State Name").title()
    
    if user_gauss == "Exit":
        missing_state = []
        for state in all_state:
            if state not in gauss_state:
                missing_state.append(state)
        # print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    
    if user_gauss in all_state:
        gauss_state.append(user_gauss)
        tim.hideturtle()
        tim.penup()
        state_data = data[data["state"] == user_gauss]
        tim.goto(state_data["x"].item(), state_data["y"].item())
        tim.write(user_gauss, align=ALIGNMENT, font=FONT)
    


# state = data[data["state"] == user_gauss]
# state_xcor = state["x"]
# print(state_xcor)
# state_ycor = state["y"]



# screen.exitonclick()