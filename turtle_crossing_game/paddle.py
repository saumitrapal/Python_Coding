from turtle import Turtle
import random

PADDLE_COLOR = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVING_DISTANCE = 5

# class MovingPaddle(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.goto(300, 0)
#         self.shape("square")
#         self.color(random.choice(PADDLE_COLOR))
#         self.shapesize(stretch_len=5, stretch_wid=1)
        
#     def move_paddle(self):
#         new_x = self.xcor() - 10
#         self.goto(new_x, 0)

class Paddle:
    def __init__(self):
        self.all_paddle = []
        self.car_speed = MOVING_DISTANCE
    
    def create_paddle(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_paddle = Turtle("square")
            new_paddle.shapesize(stretch_len=random.randint(3, 6), stretch_wid=1)
            new_paddle.penup()
            new_paddle.color(random.choice(PADDLE_COLOR))
            random_y = random.randint(-250, 250)
            new_paddle.goto(300, random_y)
            self.all_paddle.append(new_paddle)
        
    def move_paddle(self):
        for paddle in self.all_paddle:
            paddle.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVING_DISTANCE
    
                