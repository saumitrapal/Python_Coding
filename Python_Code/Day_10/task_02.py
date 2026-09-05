# Golbal Scope: ACCESSSABLE INSIDE OR OUTSIDE FOR ANY BLOCK.

num1 = 10

def sum():
    add = num1 + num1   # access a variable(num1) outside of the sum fn 
    print(f"that should be print: {add}")   # the result of this line is 10
    
sum()

print(f"that should be print: {num1}")  # the result of this line is 20


# Local Scope: ONLY VARIABLE ACCESSABLE INSIDE THR BLOCK

def sub():
    num2 = 10
    print(f"this line print: {num2}")   #this line print 10
    
sub()
print(f"this line gives a error: namespace{num2}")  # this line give us a error namespace because access a variable that is only variable inside the sub fn block.
# NameError: name 'num2' is not defined. Did you mean: 'num1'?