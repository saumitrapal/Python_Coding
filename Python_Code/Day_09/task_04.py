# calculator project
def add(frist_num, next_num):
    return frist_num + next_num

def sub(frist_num, next_num):
    return frist_num - next_num

def mul(frist_num, next_num):
    return frist_num * next_num

def divide(frist_num, next_num):
    return frist_num / next_num


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": divide
}
# my_fav_calculation = operations["*"]
# print(my_fav_calculation(4, 8))

user_operation = input("Enter the operaion +, -, *, /: ")
user_frist_number = int(input("Enter frist number: "))
user_next_number = int(input("Enter next number: "))


