from turtle import Turtle, Shape, Screen

tim = Turtle()
screen = Screen()


tim.shape("turtle")
tim.color("brown2")



# Triangle
for i in range(3):
    tim.forward(100)
    tim.left(120)


# Square
for i in range(4):
    tim.forward(100)
    tim.left(90)



# Pentagon
for i in range(5):
    tim.forward(100)
    tim.left(72)



# Hexagon
for i in range(6):
    tim.forward(100)
    tim.left(60)

# Heptagon 
for i in range(7):
    tim.forward(100)
    tim.left(51.42)
    
# Octagon
for i in range(8):
    tim.forward(100)
    tim.left(45)
    
# Nonagon
for i in range(9):
    tim.forward(100)
    tim.left(40)

# Decagon
for i in range(10):
    tim.forward(100)
    tim.left(36)



screen.exitonclick()