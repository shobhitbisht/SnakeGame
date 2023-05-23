from turtle import Turtle

class Wall(Turtle):
  def __init__(self):
    super().__init__()
    self.color("purple")
    self.hideturtle()
    self.penup()
    self.goto(300,-300)
    self.hideturtle()
    self.pendown()
    self.pensize(10)
    self.setheading(90)
    self.forward(600)
    self.setheading(180)
    self.forward(600)
    self.setheading(270)
    self.forward(600)
    self.setheading(0)
    self.forward(600)


  