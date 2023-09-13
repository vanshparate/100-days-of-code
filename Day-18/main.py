import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
# tim.shape("turtle")
directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


def spirograph(size_of_gap):
    for a in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

spirograph(5)












# for a in range(500):
#     tim.color(random_color())
#     tim.fd(30)
#     tim.setheading(random.choice(directions))



# def figures(sides, no_of_figures):
#     for a in range(no_of_figures):
#         tim.color(random.choice(colours))
#         for b in range(sides):
#             tim.right(360/sides)
#             tim.fd(100)
#         sides += 1
#
# figures(3,8)



screen = Screen()
screen.exitonclick()

