# PIZZA DELIVERY PROGRAM

print("Welcom to python pizza delivery!")
pizza_size = input("What size pizza you want? S, M or L: ")

final_bill = 0
extra_cheese_price = 1

if pizza_size == "S":
    final_bill = 15
    pepperoni_price_for_small_size = 2
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    
    if pepperoni == "Y": 
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            print(f"You final bill is: ${final_bill + pepperoni_price_for_small_size + extra_cheese_price}")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${final_bill + pepperoni_price_for_small_size}")
    
    elif pepperoni == "N":
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            print(f"Your final bill is: ${final_bill + extra_cheese_price}")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${final_bill}")
            

elif pizza_size == "M":
    final_bill = 20
    pepperoni_price_for_mediam_size = 3
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    
    if pepperoni == "Y":
        extre_cheese = input("Do you wnat extra cheese? Y or N: ")
        if extre_cheese == "Y":
            print(f"Your final bill is: {final_bill + pepperoni_price_for_mediam_size + extra_cheese_price}")       
        elif extre_cheese == "N":
            print(f"Your final bill is: ${final_bill + pepperoni_price_for_mediam_size}")
    
    elif pepperoni == "N":
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            print(f"Your final bill is: {final_bill + extra_cheese_price}")
        elif extra_cheese == "N":
            print(f"Your final bill is: {final_bill}")


elif pizza_size == "L":
    final_bill = 25
    pepperoni_price_for_large_size = 3
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    
    if pepperoni == "Y":
        extra_cheese = input("Do you extra chesse on you pizza? Y or N: ")
        if extra_cheese == "Y":
            print(f"Your final bill is: {final_bill + extra_cheese_price + pepperoni_price_for_large_size}")
        elif extra_cheese == "N":
            print(f"Your final bill is: {final_bill + pepperoni_price_for_large_size}")
            
    elif pepperoni == "N":
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            print(f"Your final bill is: {final_bill + extra_cheese_price}")
        elif extra_cheese == "N":
            print(f"Your final bill is: {final_bill}")
            
else:
    print("Sorry!")
