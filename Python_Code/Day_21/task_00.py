# list comprehension

# num_list = [1, 2, 3, 4]
# new_num_list = []
# for num in num_list:
#     num = num + 1
#     new_num_list.append(num)
# print(new_num_list)


#using list comprehension
num_list = [1, 2, 3, 4]
new_list = [num + 1 for num in num_list]    #in list comprehension: 
print(new_list)