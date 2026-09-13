from question_model import Question
from data import question_data
from quiz_brain import QuziBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    
    new_question = Question(question_text, question_answer)
    
    question_bank.append(new_question)
    
# print(len(question_bank))

quiz = QuziBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()
    
print("You completed quiz")
print(f"Your Final Score was: {quiz.score}/{quiz.question_number}")