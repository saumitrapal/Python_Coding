# define a fn call greet
# def greet():
#     print("Hello!") #print "Hello!"
#     print("Hi!")    #print "Hi!"
#     print("By!")    #print "By!"
    
# greet() #calling greet fn 


# define a fn with parameter nam
# def greet_with_parameter(nam):
#     print(f"Hello {nam}!")
#     print(f"Hi {nam}!")
    
# #calling fn with argument
# greet_with_parameter("angela")

# Parament: is name of of argument which we provided in above greet_with_name fn we pass the parament call "nam" then nam is nam of argument which we provide 
# Argument: is actull data which we provided when we calling the fn. in below when we calling fn greet_with_name fn we provided the argument call "angela"
# in brod view parament is name of data (nam) and argument is actull data(angela).abs

#fn with more than 1 parameter.
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"{name} from {location}")
    
#greet_with("angela", "england")


# in this case two parameter is here one is name and another is location.
# name(parameter) that's name of parameter that's assign a argument we provide "angela"
# location(parameter) that's name of parament that's assing a arugument we provided below "England"


# fn with keyword argument
# in keyword argument we don't need to provided argument when we calling fn.
def greet_with(name = "angela", location = "England"):
    print(f"Hello {name}!")
    print(f"{name} from {location}")

greet_with()