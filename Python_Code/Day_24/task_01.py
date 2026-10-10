import string
import random

def password_generator():

    lowercase_alphabet = list(string.ascii_lowercase)
    uppercase_alphabet = list(string.ascii_uppercase)
    decimal_number = list(string.digits)
    special_character = list(string.punctuation)

    random_choice_special_character = random.choices(special_character, k=random.randrange(start=2, stop=4))
    random_choice_lowercase_character = random.choices(lowercase_alphabet, k=random.randrange(start=2, stop=4))
    random_choice_uppercase_alphabet = random.choices(uppercase_alphabet, k=random.randrange(start=2, stop=4))
    random_choice_number = random.choices(decimal_number, k=random.randrange(start=2, stop=4))

    passwd_list = []
    passwd_list.append(''.join(random_choice_special_character))
    passwd_list.append(''.join(random_choice_lowercase_character))
    passwd_list.append(''.join(random_choice_uppercase_alphabet))
    passwd_list.append(''.join(random_choice_number))

    final_passwd_list = list(''.join(passwd_list))
    random.shuffle(final_passwd_list)
    password = ''.join(final_passwd_list)
    
    return password
   
passwd = password_generator()
