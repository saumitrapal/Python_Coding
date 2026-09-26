from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courior", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open(file="score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
         
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
      
    def reset(self):
        
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="score.txt", mode="a") as file:
                file.write(f"\n{self.high_score}")
                
        self.score = 0
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    