print(len("1234"))  #print the lenght of string which we provided


name = "Hello"  # store the string value on name variable
print(type(name))   # print the value type using type() function that tell us the type of value which we provided

intNum = 123    # store the integer value on intNum variable
print(type(intNum)) # print the value type usign type function that tell us the type of value which we provided

floatNum = 3.1415   # store the float value on floatNum variable
print(type(floatNum))   # print the value type using type function that tell us the type of value which we provided 

boolValue = True    # store the boolean value on boolValue variable
print(type(boolValue))  # print the value type using type function that tell us the type of claue which we provide


# TYPE CONVERSION: conver a another type of data into other type like string "123" to 123

print(int("123") + int("345"))  # this frist conver into string to integer and then add those integer and give us a result as a 468


str()
int()
float()
bool()

#print("Number of letter on your name: " + len(input("Enter your name: ")))  #this line print
#using plus we only concatenates string not an integer number

# Enter your name: hello
# Traceback (most recent call last):
#   File "/home/saumitrapal/Learn_Python/Python_Code/Day_01/task_01.py", line 27, in <module>
#     print("Number of letter on your name: " + len(input("Enter your name: ")))
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TypeError: can only concatenate str (not "int") to str


print("Number of letter on your name: ", len(input("Enter your name: ")))   #this line print our desire result