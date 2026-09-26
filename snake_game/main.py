import turtle, random, time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# for position in starting_position:
#     new_segment = turtle.Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)

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
    
    #snake collision with food
    if snake.head.distance(food) < 15:
        food.refrash()
        snake.extand_sanke()
        scoreboard.increase_score()
        
    #snake collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()
        # is_game_on = False
    elif snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        # is_game_on = False
    
    #snake colide with tail
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            # is_game_on = False
            scoreboard.reset()
            snake.reset()
    
    
screen.exitonclick()