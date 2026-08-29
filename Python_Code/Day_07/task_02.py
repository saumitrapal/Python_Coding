# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 

def calculate_love_score(name1, name2):
    combine_name = name1 + name2
    lower_combine_name = combine_name.lower()
    
    t = lower_combine_name.count("t")
    r = lower_combine_name.count("r")
    u = lower_combine_name.count("u")
    e = lower_combine_name.count("e")
    
    true_score_int = t + r + u + e
    
    l = lower_combine_name.count("l")
    o = lower_combine_name.count("o")
    v = lower_combine_name.count("v")
    e = lower_combine_name.count("e")
    
    love_score_int = l + o + v + e
    
    final_love_score_str_combine = str(true_score_int) + str(love_score_int)
    
    print(final_love_score_str_combine)
    
    
calculate_love_score("Kanye West", "Kim Kardashian")