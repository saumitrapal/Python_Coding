# TREASUREISLAND GAME


# this is ASCII art for https://ascii.co.uk/art/treasureisland and note this is an multiline print statement
# when we want to print multiline statement then we usally statement sit under ''''''. to print multiple line.
print('''
         /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%
      ''')

print("==============================================================================================================================================================")

print("Welcome to Treasure Island!")
user_choice = input("Welcome to Treasure Island.Your mission is to find the treasure: 'left' or 'right': ")


# HERE I CHOISE .lower() fn because of i dont know which case is wirte a user if is uppercase then it convert lowercase 'left'
# if user put Left then is this program actcept lowercase left.
if user_choice.lower() == 'left':
    user_decision = input('You\'ve come to lake there is an island in the middle of the lake. Type "wait" for a boat or Type "swim" to swim across: ')
    if user_decision.lower() == 'wait':
        user_color_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: ")
        if user_color_choice.lower() == 'yellow':
            print("You found the treasure! You Win!")
        elif user_color_choice.lower() == 'red':
            print("It's a room full of fire. Game Over!")
        elif user_color_choice.lower() == 'blue':
            print("Your enter a room of beasts. Game Over!")
        else:
            print("You Got Attact By Anger Trout. Game Over!.")
    else:
        print("You get attacked by an angry trout. Game Over!.")
else:
    print("You fell into a hole. Game Over!")