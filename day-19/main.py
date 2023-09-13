from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y_pos = [75, 45, 15, -15, -45, -75]
all_turtle = []
for x in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[x])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

"""Code to move turtle with WASD keys"""
# screen.listen()
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_left():
#     tim.right(10)
#
# def turn_right():
#     tim.left(10)
#
# def reset_turtle():
#     tim.reset()
#
# screen.onkey(key="W", fun=move_forward)
# screen.onkey(key="S", fun=move_backward)
# screen.onkey(key="A", fun=turn_left)
# screen.onkey(key="D", fun=turn_right)
# screen.onkey(key="C", fun=reset_turtle)
screen.exitonclick()
