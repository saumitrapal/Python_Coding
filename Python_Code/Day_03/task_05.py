# Rock Paper Scissors (RPS) is one of the world's most recognized hand games - played by billions across every culture. 
# Two players simultaneously form one of three shapes: a fist (rock), a flat hand (paper), or a V (scissors). 
# Rock crushes scissors, scissors cuts paper, and paper covers rock.

import random

print("Welcome to ROCK, PAPER, SCISSORS GAME!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

# Rock crushes scissors, scissors cuts paper, and paper covers rock.
# Rock(0), Paper(1), Scissors(2):

# user_decision_list = ["Rock", "Paper", "Scissors"]
user_input = int(input("Enter a number 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_input = random.randint(0, 2)

if user_input == 0 and computer_input == 0:
    print(f"You entet {user_input}\n {rock} \n and computer enter {computer_input} {rock}.\n Draw Match!")
elif user_input == 0 and computer_input == 1:
    print(f"You enter {user_input}\n {rock} \n and computer enter {computer_input}\n {paper}.\n You Loss!")
elif user_input == 0 and computer_input == 2:
    print(f"You enter {user_input}\n {rock}\n and computer enter {computer_input}\n {scissors}.\n You Win!")
elif user_input == 1 and computer_input == 0:
    print(f"You enter {user_input}\n {paper}\n and computer enter {computer_input}\n {rock}.\n You Win!")
elif user_input == 1 and computer_input == 1:
    print(f"You entet {user_input}\n {paper}\n and computer enter {computer_input}\n {paper}.\n Draw Match!")
elif user_input == 1 and computer_input == 2:
    print(f"You enter {user_input}\n {paper}\n and computer enter {computer_input}\n {scissors}.\n You Loss!")
elif user_input == 2 and computer_input == 0:
    print(f"You enter {user_input}\n {scissors}\n and computer enter {computer_input}\n {rock}.\n You Loss!")
elif user_input == 2 and computer_input == 1:
    print(f"you enter {user_input}\n {scissors}\n and computer enter {computer_input}\n {paper}.\n You Win!")
elif user_input == 2 and computer_input == 2:
    print(f"You entet {user_input}\n {scissors}\n and computer enter {computer_input}\n {scissors}.\n Draw Match!")
else:
    print("Sorry! ONLY ENTER 0, 1, 2 NUMBER")