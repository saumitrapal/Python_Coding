from turtle import Turtle, Shape, Screen

tim = Turtle()
screen = Screen()


tim.shape("turtle")




# Triangle
for i in range(3):
    tim.color("brown2")
    tim.forward(100)
    tim.right(120)


# Square
for i in range(4):
    tim.color("purple")
    tim.forward(100)
    tim.right(90)



# Pentagon
for i in range(5):
    tim.color("black")
    tim.forward(100)
    tim.right(72)



# Hexagon
for i in range(6):
    tim.color("brown1")
    tim.forward(100)
    tim.right(60)

# Heptagon 
for i in range(7):
    tim.color("green")
    tim.forward(100)
    tim.right(51.42)
    
# Octagon
for i in range(8):
    tim.color("red")
    tim.forward(100)
    tim.right(45)
    
# Nonagon
for i in range(9):
    tim.color("orange")
    tim.forward(100)
    tim.right(40)

# Decagon
for i in range(10):
    tim.color("blue")
    tim.forward(100)
    tim.right(36)



screen.exitonclick()