# ceaser cipher encrption

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

def encryption():
    word = input("Enter a word for encrypt: ")
    user_input = int(input("Enter how many letter you want to shift: "))
    
    # find index of each char from word from the list called letters and append into list.
    index_list = []
    for char in word:
        index_list.append(letters.index(char))
    # print(index_list)
    
    #shift right each char by user input number and append into list.
    index_list_shift = []
    for num in range(0, len(index_list)):
        index_list_shift.append(index_list[num] + user_input)
    # print(index_list_shift)

    #find each shifted char into list called letters
    shift_letter = []
    for i in range(0, len(index_list_shift)):
        shift_letter.append(letters[int(index_list_shift[i])])
    # print(shift_letter)    
    
    #join the list of char and get final word
    final_word = ''.join(shift_letter)
    
    #print final word
    print(f"Your Encrypted Word Is: {final_word} ")
        
                   
def decryption():
    word = input("Enter a word for encrypt: ")
    user_input = int(input("Enter how many letter you want to shift: "))
    
    # find index of each char from word from the list called letters and append into list.
    index_list = []
    for char in word:
        index_list.append(letters.index(char))
    # print(index_list)
    
    #shift left each char by user input number and append into list.
    index_list_shift = []
    for num in range(0, len(index_list)):
        index_list_shift.append(index_list[num] - user_input)
    # print(index_list_shift)

    #find each shifted char into list called letters
    shift_letter = []
    for i in range(0, len(index_list_shift)):
        shift_letter.append(letters[int(index_list_shift[i])])
    # print(shift_letter)    
    
    #join the list of char and get final word
    final_word = ''.join(shift_letter)
    
    #print final word
    print(f"Your Encrypted Word Is: {final_word} ")


print("Welcome To Ceaser Ciapher Encoding And Decoding!")

should_continue = True

while should_continue:
    user_input_operation = input("Enter Which Operation You Want To Parfrom 'encode' for encryption OR 'decode' for deccryption: ")
    
    if user_input_operation == "encode":
        encryption()
    elif user_input_operation == "decode":
        decryption()
    else:
        print("SORRY! enter valid input")
    
    user_continue = input("Type 'yes' if you want to go again and Type 'no' Otherwise: ").lower()
    if user_continue == "no":
        should_continue = False
        print("GoodBye!")
    else:
        user_continue
        
    
