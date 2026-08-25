#FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

start = 0
str1 = "Fizz"
str2 = "Buzz"

for num in range(1, 101):
    num += start

    if num % 3 == 0 and num % 5 == 0:
        print(f"{str1 + str2}")
    elif not(num % 3 == 0) and (num % 5 == 0):
            print(f"{str2}")
    elif (num % 3 == 0) and not(num % 5 == 0):
            print(f"{str1}")
    else:
        print(num)