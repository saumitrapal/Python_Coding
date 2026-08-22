# MODULO OPERATOR
num1 = 9
num2 = 3

print(num1 % num2)  #result is 0 because no remainder is left


#ODD AND EVEN CHECK
num = int(input("What number you want to check: ")) # type conversion string to integer.


result = num % 2

print(type(result))

# condition check for even or odd
if result == 0:
    print("Your provided number is even.")
else:
    print("Your provided number is not even.")