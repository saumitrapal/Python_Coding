# PASSWORD GENERATOR PROJECT
import random


print("Welcome To Random Password Generator!")

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

user_input_for_password = int(input("Enter how long password you want: "))
user_input_for_letter = int(input("Enter how much letter want in your password: "))
user_input_for_number = int(input("Enter how many number you want in your password: "))
user_input_for_special_characters = int(input("Enter how many special characters you want in your password: "))

# EASY PASSWORD GENERATOR

# if user_input_for_password == (user_input_for_letter + user_input_for_number + user_input_for_special_characters):
#     password_letter = ""
#     password_number = ""
#     password_sp_char = ""
#     final_password = ""

#     for char in range(0, user_input_for_letter):
#         random_letter = random.choice(letters)
#         password_letter = password_letter + random_letter
    
#     for num in range(0, user_input_for_number):
#         random_number = random.choice(numbers)
#         password_number = password_number + random_number

#     for sp_char in range(0, user_input_for_special_characters):
#         random_special_char = random.choice(special_characters)
#         password_sp_char = password_sp_char + random_special_char

#     random_generate_password = password_letter + password_number + password_sp_char
    
#     print("Your Random Generate Password Is With Your Choice Length: " + random_generate_password)
# else:
#     print("Your password lenght not match the lenght of letter, number, special characters you enter!")



# HARD PASSWORD GENERATOR

if user_input_for_password == (user_input_for_letter + user_input_for_number + user_input_for_special_characters):
    
    password_list = []
    result_password = ""

    for char in range(0, user_input_for_letter):
        password_list.append(random.choice(letters))
    
    for num in range(0, user_input_for_number):
        password_list.append(random.choice(numbers))

    for sp_char in range(0, user_input_for_special_characters):
        password_list.append(random.choice(special_characters))

    random.shuffle(password_list)
        
    for char in password_list:
        result_password = result_password + char
    print(f"Your Random Generate Password Is With Your Choice Length: {result_password}")
    
else:
    print("Your password lenght not match the lenght of letter, number, special characters you enter!")