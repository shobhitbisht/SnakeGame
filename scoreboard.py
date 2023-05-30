from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20 , 'normal')

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.color("purple")
    self.hideturtle()
    self.penup()
    self.goto(0,260)
    self.score = 0
    self.highscore = 0
    self.show_score()

  def show_score(self):
    self.clear()
    self.write(f"Score : {self.score} High Score: {self.highscore}", align = ALIGNMENT, font = FONT)

  def reset(self):
    if self.score > self.highscore:
      self.highscore = self.score

    self.score = 0
    self.show_score()
    

  def increase_score(self):
    self.score += 1
    self.show_score()
   
    
