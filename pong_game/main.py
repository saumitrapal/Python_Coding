from turtle import Turtle, Screen   #import require module
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()   #assign Screen() class to screen variable
screen.setup(width=800, height=600) #screen setup with height and width
screen.bgcolor("black") #screen background "black"
screen.title(titlestring="PONG GAME")   #screen title "PONG GAME"
screen.tracer(0)    #trun off animation or animation is on in backgroud but not visible

paddle = Turtle()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update() # update after animation is created
    time.sleep(ball.move_speed)
    ball.move_ball()
    
    # collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        
        
    # collision with the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        
    # right paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #left paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
    #show score



screen.exitonclick()    #click to exit from screen