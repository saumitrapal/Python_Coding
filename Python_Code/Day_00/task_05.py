# We have 2 variables glass1 and glass2. 
# glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". 
# You are only allowed to use variables to solve this exercise. 

glass1 = "milk"
glass2 = "juice"

# Create a temp variable that hold glass1 value
temp = glass1
# print(temp)
# Now assign glass2 value into glass1
glass1 = glass2
# print(glass1)
# Atlast assign the value temp into glass2
glass2 = temp
# print(glass2)

print(glass1, glass2)



# Number swap without using third variable
int1 = 4
int2 = 5

int1 = int1 - int2
# int1 = 4 - 5 = -1
int2 = int2 + int1
# int2 = 5 - 1 = 4 // because int1 become -1 from above line
int1 = int2 - int1
# int1 = 4 - (-1) = 5 // because int2 become 4 from above line

print(int1, int2)