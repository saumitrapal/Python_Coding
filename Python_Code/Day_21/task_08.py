import pandas

student_data = {
    "student_name": ["Alex", "Beth", "Cathrine", "Dave", "Eval", "Fon"],
    "student_score": [40, 50, 60, 70, 80, 90]
}
data = pandas.DataFrame(student_data)
# print(data)

# challenges: store student data corrosponding to student name, student score into dictonary
student_dict = {name: score for (name, score) in student_data.items()}
print(student_dict)