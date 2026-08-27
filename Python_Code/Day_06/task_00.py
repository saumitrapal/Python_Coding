# WORD GAUSSING GAME

hangman = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

============================================================================
'''

print(hangman)

hangman_hang = []
gauss_word = []
i = 0
word = "cat"
split_word = list(word)
split_word_lenght = len(split_word)

while split_word_lenght > 0:
    user_letter_input = input("Enter a Letter: ")
    conver_user_letter_to_lowercase = user_letter_input.lower()
    store_user_input = gauss_word.append(conver_user_letter_to_lowercase)
   
    split_word_lenght -= 1

join_word = ''.join(split_word)
join_gauss_word = ''.join(gauss_word)

for i in range(0, 1):
    if join_word == join_gauss_word:
        print("Correct!", join_word, join_gauss_word)
    else:
        print("Worng!", join_word, join_gauss_word)
            
