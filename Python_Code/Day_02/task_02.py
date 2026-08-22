# NESTED CONDITION 
# CHECK ROLLERCOSTER RIDE GAME

print("Welcome to Rollercoster Ride!")

height = int(input("Enter your height: "))

if height >= 120:
    print("Your are allow to do Rollercoster Ride.")
    age = int(input("Enter your age."))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Your are not allow to do Rollercoster Ride.")
    