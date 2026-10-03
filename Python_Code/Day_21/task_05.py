# Dictonary Comprehension
# dict = {}
# new_dict = {new_key: new_value for (key, value) in dict if test}
import random

student_names = ["Alex", "Beth", "Caroline", "Dave", "Eval", "Fon"]

student_list = {student: random.randint(50, 100) for student in student_names}
passed_student = {student: value for (student, value) in student_list.items() if value > 70}
print(student_list)
print(passed_student)