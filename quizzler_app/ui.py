from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, height=600, width=700)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 24, "normal"))
        self.score_label.grid(row=0, column=1, pady=24)
        
        self.canvas = Canvas(self.window, width=400, height=500, bg="white")
        self.canvas.grid(row=1, column=0, padx=100, pady=48, columnspan=2)
        self.question_text = self.canvas.create_text(200, 250, text="Hello", font=("Arial", 20, "bold"), fill=THEME_COLOR, width=350)
        
        self.wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_btn = Button(image=self.wrong_img, command=self.false_pressed)
        self.wrong_btn.grid(row=2, column=1)
        
        self.right_img = PhotoImage(file="./images/true.png")
        self.right_btn = Button(image=self.right_img, command=self.true_pressed)
        self.right_btn.grid(row=2, column=0)
        
        self.get_next_question()
    
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the quiz.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
        
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("Talse") 
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)
    