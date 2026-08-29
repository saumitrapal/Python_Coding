import random
from replit import clear
import task_05 as import_file

print("Welcome to Hangman Game!")
print(import_file.logo)

stages = import_file.ascii_art
word_list = import_file.words  # provided list
chosen_word = random.choice(word_list)  # randomly choice word from list call word_list
print(chosen_word)
display = []
word_length = len(chosen_word)

for i in range(0, word_length):
    display += "_"
print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guass = input("Guass a letter: ").lower()
    
    if guass in display:
            print(f"You already guassed letter {guass}")

    clear() #that clear() fn clear my terminal display every time i guassed a letter.
            
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guass:
            display[position] = letter
     
    if guass not in chosen_word:
        lives -= 1
        print(f"You guassed {guass}, that's not in the word. you loss a life.")
        if lives == 0:
            end_of_game = True
            print("You loss!")
        
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(display)
    
    
    
    print(stages[lives])
