from turtle import Turtle
import random
#Food class inherited from Turtle class
class Food(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    #resizing the turtle
    self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
    self.color("blue")
    # self.speed("fastest")
    #calling refresh method so that in starting of each game 
    #location of food will be different
    self.refresh()
  #genrates random int and sets it on goto menthod
  #to place food at random place in each iteration
  def refresh(self):
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x,random_y)