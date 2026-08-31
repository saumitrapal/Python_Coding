# function with multiple output

def format_name(frist_name, last_name):

    frist_name_titel_case = frist_name.capitalize()
    last_name_titel_case = last_name.capitalize()
    full_name = frist_name_titel_case + " " + last_name_titel_case
    
    if frist_name_titel_case == "" and last_name_titel_case == "":
        return "You didn't provided any input"
    else:
        return full_name
    
output_format_name = format_name(input("Enter Your Frist Name: "), input("Enter Your Last Name: "))
print(output_format_name)
    