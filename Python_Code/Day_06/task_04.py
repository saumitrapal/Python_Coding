import random

word_list = ["apple", "pear", "green", "red", "black"]  # provided list
chosen_word = random.choice(word_list)  # randomly choice word from list call word_list
display = []
word_length = len(chosen_word)

for i in range(0, word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guass = input("Guass a letter: ").lower()
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guass:
            display[position] = letter  
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(display)
