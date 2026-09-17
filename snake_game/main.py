import turtle, random, time
from snake import Snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# for position in starting_position:
#     new_segment = turtle.Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.snake_up)
screen.onkey(key="Down", fun=snake.snake_down)
screen.onkey(key="Right", fun=snake.snake_right)
screen.onkey(key="Left", fun=snake.snake_left)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move_snake()




















screen.exitonclick()