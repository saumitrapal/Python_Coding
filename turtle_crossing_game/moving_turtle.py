from turtle import Turtle
FINISH_LINE_Y = 280
MOVING_DISTANCE = 10

class TurtleMove(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.goto(0, -280)
        # self.go_to_star()
        self.penup()
        self.shape("turtle")
        self.color("#ffffff")
    
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)
        # self.forward(MOVING_DISTANCE)
        
    def go_to_star(self):
        self.goto(0, -280)
        
    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(0, new_y)
        
    def is_at_finished_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False