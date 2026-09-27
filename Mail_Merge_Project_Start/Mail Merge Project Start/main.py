#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
    
PLACEHOLDER = "[name]"   

with open(file="./Input/Letters/starting_letter.txt", mode="r") as file:
    content_list = file.read()
    # print(content_list)
with open(file="./Input/Names/invited_names.txt", mode="r") as file:
    name_list = file.readlines()
    # print(name_list)
    for name in name_list:
        striped_name = name.strip()
        replace_line = content_list.replace(PLACEHOLDER, striped_name)
        # print(replace_line)
        with open(file=f"./Output/ReadyToSend/letter_for_{striped_name}.docx", mode="w") as file:
            file.write(replace_line)


