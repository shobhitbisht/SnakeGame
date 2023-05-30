from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall

# Importing time module to use sleep method.
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=400, height=400)
screen.title("The Snake Game")

# Tracer is a method which traces screen and gives it output
screen.tracer(0)

#object of wall which will creates a boarder on screen
wall = Wall()

#object of snake class which will create a snake body using 3 turtle objects
snake = Snake()

#object of food class which creates a food.
food = Food()

#object of scoreboard class which creates a scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
# ^
# |
# Main game loop by default is True/on with help of game_is_on var.
# So that game can run atleast once.
# Here if we don't use tracer and update method then our snake
# segments/turtle will move one by one instead of moving together.
while game_is_on:

  #update method will show all movements/animation/drwaing done
  #after tracer was off tracer(0) till update method is called.
  screen.update()

  #sleep will pause the movement/ drwaing for particular time.
  #The code written after this func will pause for the time mentioned between paretheses()
  time.sleep(0.1)

  #Move function from class sanke which moves each seg of snake together
  snake.move()

  #Detech colision with food
  if snake.head.distance(food) < 15:
    #after the collision with food
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  #Detech collision with wall.
  if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor(
  ) > 298 or snake.head.ycor() < -298:

    scoreboard.reset()
    snake.reset()

  #Detech collision with tail
  for segment in snake.segments[1:]:

    #used distance method to detch the collison between head and other segments of snake body
    if snake.head.distance(segment) < 10:

      scoreboard.reset()
      snake.reset()
