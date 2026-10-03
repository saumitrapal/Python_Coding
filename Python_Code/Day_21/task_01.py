name = "Angela"
#using list comprehension
letter_list = [letter for letter in name]
print(letter_list)


new_numbers_list = [(num * 2) for num in range(1, 5)]
print(new_numbers_list)



#conditional list comprehension
name_list = ["Alex", "Beth", "Caroline", "Dave"]
#only name start with "A" letter
new_name_list = [name for name in name_list if name[0] == "A"]
# this line of code print name which lenght is greter than 5 in uppercase
new_name_uppercase = [name.upper() for name in name_list if len(name) > 5]
print(new_name_uppercase)
print(new_name_list)