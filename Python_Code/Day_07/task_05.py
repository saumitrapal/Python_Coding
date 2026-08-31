#Keep taking numbers as inputs till the user enters ‘x’,
# after that print sum of all.
def sum():
    num = int(input("Enter a number: "))
    result = 0
    for i in range(0, num + 1):
        result = result + i
    print(f"Sum of frist natural number: {result}")
sum()