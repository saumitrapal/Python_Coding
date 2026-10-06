# *args means n number of argument 

#this fn takes n numbers of arugument add those n number of aruguments and return result
def add(*args):
    result = 0
    for num in args:
        result = result + num    
    return  result
    
sum = add(1, 2, 3, 4, 5, 6, 7 ,8 ,9)
print(sum)