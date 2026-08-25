# WHO THE BILL GAME USING RANDAMIZATION.
import random   #import random module

print("Welcome to Who Pay The Bill Game!")  #print as it is

name_of_people = ["Angela", "Bill", "Jenny", "Michael", "Chloe"]    #list define in python and name of list name_of_people.

lenght_of_name_list = len(name_of_people)   #lenght of name_of_people using len() fn that give us lenght of lists

choose_name_randomly = random.randint(0, (lenght_of_name_list - 1)) #print the number in between 0 and 9lenght of lists - 1).

pay_bill_name = name_of_people[choose_name_randomly]    #choose the name of people from the list.

print(f"{pay_bill_name} is going to buy the meal today!")   #print the name using f-string.