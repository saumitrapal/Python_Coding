import turtle
MOVE_DISTANCE = 20
UP = 90
DONW = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]
    
    def creat_snake(self):
        for position in range(3):
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        for position in range(3):
            new_segment.goto(-20 * position, 0)
            self.segments.append(new_segment)
        
    def extand_sanke(self):
        self.add_segment(self.segments[-1].position())
            
    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)     
        self.segments[0].forward(MOVE_DISTANCE)
        
    def snake_up(self):
        if self.head.heading() != DONW:
            self.head.setheading(UP)
    
    def snake_down(self):
        if self.head.heading != UP:
            self.head.setheading(DONW)
    
    def snake_right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)
    
    def snake_left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)