# Black Jack Project
import random
import math

user_decision = input("Do you want to play BlackJacl y or n: ")

if user_decision == 'y':
    user_random_number_list = []
    comp_random_number_list = []
    

    user_random_number_list.append(random.randint(1, 10))
    user_random_number_list.append(random.randint(1, 10))
    
    comp_random_number_list.append(random.randint(1, 10))
    comp_random_number_list.append(random.randint(1, 10))

    print(f"Your initial card: {user_random_number_list}")
    print(f"computer initial card: {comp_random_number_list[0]}")
    print(sum(user_random_number_list))
    print(sum(comp_random_number_list))

    
    game = True
    comparision_number = 21
    
    
    while game:
        get_another_card = input("Type 'y' to get another card or Type 'n' to pass: ")
        
        comp_random_number_list.append(random.randint(1, 10))
        if get_another_card == 'y':
            user_random_number_list.append(random.randint(1, 10))
            
            # print(sum(random_num1))
            print(user_random_number_list)
            print(comp_random_number_list)
            print(sum(user_random_number_list))
            print(sum(comp_random_number_list))
            print(f"computer initial card: {comp_random_number_list[0]}")
            
        else:
            print(user_random_number_list)
            print(comp_random_number_list)
            print(sum(user_random_number_list))
            print(sum(comp_random_number_list))   
            game = False
            

    
        
