# multiple list item by two

def list_multiply(user_list):
	b_list = []
	for i in user_list:
		b_list.append(i * 2)
	
	return b_list 

print_b_list = list_multiply([1, 2, 3, 4])
print(print_b_list)