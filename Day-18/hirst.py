# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.ht()
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
tim.speed('fastest')
tim.setheading(225)
tim.penup()
tim.fd(300)
tim.setheading(0)

def next_line():
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.left(180)

for x in range(10):
    for a in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    next_line()


screen = Screen()
screen.exitonclick()