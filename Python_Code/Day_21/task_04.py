# Data Overlap
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 
# e.g. if file1.txt contained: 
# 1 
# 2 
# 3
# and file2.txt contained: 
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop.  \
# [3, 6, 5, 33, 12, 7, 42, 13]

with open(file="file1.txt", mode="r") as file:
    file1_content = file.read()
    str_list_of_number = file1_content.split()
    num1_list = [int(num ) for num in str_list_of_number]
    # num1_list.sort()
    # print(num1_list)
    
with open(file="file2.txt", mode="r") as file:
    file2_content = file.read()
    str_list_of_number = file2_content.split()
    num2_list = [int(num) for num in str_list_of_number]
    # num2_list.sort()
    # print(num2_list)
    # print(num2_list)

result = [num for num in num1_list if num in num2_list]
print(f"The intersection list is: {result}")


# for num in num1_list:
#     if num in num2_list:
#         print(num)


