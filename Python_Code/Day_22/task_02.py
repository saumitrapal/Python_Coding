# **kwargs means keyword arguments. it takes n number arguments with the form of keyword.

def add(**kwargs):
    result = 0
    for key, value in kwargs.items():
        result = result + value
    return result
        
sum = add(a=1, b=2, c=3, d=4, e=5)
print(sum)
