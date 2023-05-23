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
    self.show_score()

  def show_score(self):
    self.write(f"Score : {self.score}", align = ALIGNMENT, font = FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align = ALIGNMENT, font = FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.show_score()
   
    
