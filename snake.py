from turtle import Turtle

MOVE_DIST = 20
'''list of positions in tuple form of x and y coordinate
which will be used as input for goto menthod'''
START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self):
    
    # Empty list which will store turtle objects later
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
  #This func will create a default snake with 3 segments
  def create_snake(self):
    # Forloop to create 3 different turtle/segments of square shape
    # and placing them together one by one""" 
    for pos in START_POS:
      self.add_segment(pos)

    #This fuction will create a new segment
  def add_segment(self, pos):
      turt = Turtle("square")
      turt.color("white")
      turt.penup()
      turt.goto(pos)
      self.segments.append(turt)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  def up(self):
    #used this if statement so that sake can't move backwards on same line
    #heading() returns current head direction of turtle object(Segment)
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
     
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
   
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
   
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
         
  def move(self):
    
    #Using reverse loop trough each segment/turtle and moving them one by one.
    #All seg except first will follow the cords of seg ahead them.
    #First seg will move in direction where ever we want it to move.
    #Using xcor and ycor will extract cords of other segments.
    #Using goto will move other cords to location of a seg ahead them.
    #MAKED THE TAIL OF THE SNAKE TO FOLLOW IT'S HEAD
    for seg_num in range(len(self.segments)-1,0,-1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
       
    self.head.forward(MOVE_DIST)
    

  def reset(self):
    for segment in self.segments:
      segment.goto(2000,2000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]