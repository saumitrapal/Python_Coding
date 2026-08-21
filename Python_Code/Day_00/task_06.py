# SMALL PROJECT: create a brand name generator 
# that take input type string from user as where they live, there pet name.
# combin this user input string and print the name of brand

# this line print following string
print("Welcome To Brand Name Generator!")

# take input from user where they lived as type string
lived = input("Enter where you live: \n=> ")
# print(lived)

# take input from user there pet name as type of string
petName = input("Enter your pat name: \n=> ")
# print(patName)


# combine(concatenate string using +) user input
brandName = lived + petName


# print brand name
print("Your brand name is following: " +brandName)