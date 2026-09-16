import turtle

tim = turtle.Turtle()
screen =turtle.Screen()

def move_tim_forward():
    tim.forward(100)
    
def move_tim_clear_draw():
    tim.clear()

def move_tim_backward():
    tim.backward(100)
    
def move_tim_counterclockwise():
    tim.right(10)
    
def move_tim_anticlockwise():
    tim.left(10)
    
def tim_move_reset():
    tim.reset()
    


screen.listen()
screen.onkey(key="w", fun=move_tim_forward)
screen.onkey(key="s", fun=move_tim_backward)
screen.onkey(key="a", fun=move_tim_counterclockwise)
screen.onkey(key="d", fun=move_tim_anticlockwise)
screen.onkey(key="c", fun=move_tim_clear_draw)
screen.onkey(key="r", fun=tim_move_reset)
screen.exitonclick()

