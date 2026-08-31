def format_name(first_name, last_name):
    
    # .capitalize() fn conver capital word to titel case like Angela or Yu
    full_name = first_name.capitalize() + " " + last_name.capitalize()
    
    return full_name

output_format_name = format_name("ANGELA", "YU")
print(output_format_name)