# Number Gaussing Game 
import random

print("Welcome To Number Gaussing Game!")

def easy_mode():
    random_number = random.randint(1, 100)
    # print(random_number)
    gauss = 10
    print(f"You have only {gauss} chance! for easy mode")
    while gauss:
        
        user_gauss_number = int(input(f"Enter a number between 1 to 100 you have only {gauss} chance left: "))
        
        if random_number == user_gauss_number:
            print("You gauss the number")
            restart_game = input("Type 'y' for play game again or 'n' for exit: ")
            if restart_game == 'y':
                mode()
            elif restart_game == 'n':
                break
            
        elif random_number < user_gauss_number:
            print(f"You number is higher {user_gauss_number}")
        elif random_number > user_gauss_number:
            print(f"Your number is lower {user_gauss_number}")
        
        gauss = gauss - 1
        
def hard_mode():
    random_number = random.randint(1, 100)
    # print(random_number)
    gauss = 5
    print(f"You have only {gauss} chance! for hard mode")
    while gauss:
        
        user_gauss_number = int(input(f"Enter a number between 1 to 100 you have only {gauss} chance left: "))
        
        if random_number == user_gauss_number:
            print("You gauss the number")
            
            restart_game = input("Type 'y' for play game again or 'n' for exit: ")
            if restart_game == 'y':
                mode()
            elif restart_game == 'n':
                break
            
        elif random_number < user_gauss_number:
            print(f"You number is higher {user_gauss_number}")
        elif random_number > user_gauss_number:
            print(f"Your number is lower {user_gauss_number}")
        
        gauss = gauss - 1
        
  
        
def mode():
    user_mode = input("Enter which mode you want to play 'easy' or 'hard': ")
    if user_mode == "easy":
        easy_mode()
    elif user_mode == "hard":
        hard_mode()
        
mode()
