# HANGMAN

import random

head = '''
        ______
        |     |
        O     |
              |
              |
              |
              |
    ---------------------
'''

body = '''
        |
        |
        |
'''

left_hand = '''
        /
'''

right_hand = '''
        \
'''
right_lag = '''
            \
'''

left_lag = '''
    /
'''

hangman = [head, body, left_hand, right_hand, left_lag, right_lag]
lenght_hangman = len(hangman)
add_dash = []
word_list = ["apple", "apply", "ape", "ample", "banana", "application"]
randomly_choice_word = random.choice(word_list)
split_by_char = list(randomly_choice_word)
lenght_of_split_word = len(split_by_char)

while lenght_of_split_word > 0:
    add_dash.append("_")
    lenght_of_split_word -= 1

join_dash = ' '.join(add_dash)

print(join_dash)

user_input_list = []
while len(hangman) > 0:
    user_input = input("Enter a Letter: ")
    user_input_letter_list = user_input_list.append(user_input)
    
    # if user_input == split_by_char:
    #     add_dash.append(user_input)
    # else:
    #     print(hangman[0])
    
    lenght_hangman -= 1
print(user_input_list)
