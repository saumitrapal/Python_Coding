#function
# how many weeks are left from current age. if you live 90

def life_in_weeks(age):
    total_weeks = 90 * 52
    user_week = age * 52
    final_week_remain = total_weeks - user_week
    print(f"You have {final_week_remain} weeks left.")
    
    
life_in_weeks(56)