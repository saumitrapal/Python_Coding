from turtle import Screen
import time
from moving_turtle import TurtleMove
from paddle import Paddle
from scoreboard import Scroeboard

screen = Screen()
screen.setup(width=600, height=800)
screen.tracer(0)
screen.bgcolor("#000000")
moving_turtle = TurtleMove()
moving_paddle = Paddle()
socreboard = Scroeboard()

screen.listen()
screen.onkey(moving_turtle.move_up, "Up")
screen.onkey(fun=moving_turtle.move_down, key="Down")
    
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    moving_paddle.create_paddle()
    moving_paddle.move_paddle()

    #detect coilsion with the car
    for paddle in moving_paddle.all_paddle:
        if paddle.distance(moving_turtle) < 20:
            is_game_on = False
            socreboard.game_over()
            
    #detected successful crossing 
    if moving_turtle.is_at_finished_line():
        moving_turtle.go_to_star()
        moving_paddle.level_up()
        socreboard.increase_level()
            
screen.exitonclick()