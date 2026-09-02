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


def calculation():
    '''
    calculator function
    '''
    
    should_acumulate = True
    # frist input from user
    user_frist_number = int(input("Enter frist number: "))
    
    while should_acumulate:
        
        # operation input from user
        user_operation = input("Enter the operaion +, -, *, /: ")
        # second input from user
        user_next_number = int(input("Enter next number: "))
        # answer of calculation
        answer = operations[user_operation](user_frist_number, user_next_number)
        # print answer in 5 + 3 = 8 format
        print(f"{user_frist_number} {user_operation} {user_next_number} = {answer}")

        # take input y or n from user 
        continue_operation = input(f"Type 'y' for perform operations with {answer} or Type 'n' for new operations: ")
                
        # if y then store answer into user frist input if no then it break while loop to false
        if continue_operation == 'y':
            user_frist_number = answer
        else:
            should_acumulate = False
            print("\n " * 20)
            calculation()   # using recursion fn call multiple times

# calling fn
calculation()
            
        
        
        
        

