from turtle import Turtle, Screen
import os

tim = Turtle()
screen = Screen()

def move_forward():
    tim.pendown()
    tim.forward(50)
def move_backward():
    tim.pendown()
    tim.back(50)
def counter_clockwise():
    tim.pendown()
    tim.left(10)
def move_clockwise():
    tim.pendown()
    tim.right(10)
def clear():
    tim.home()
    tim.clear()
    

screen.listen()
screen.onkey(key="w", fun=(move_forward))
screen.onkey(key="s", fun=(move_backward))
screen.onkey(key="a", fun=(counter_clockwise))
screen.onkey(key="d", fun=(move_clockwise))
screen.onkey(key="c", fun=(clear))



screen.exitonclick()