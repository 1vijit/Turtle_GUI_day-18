###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random
from turtle import Screen

t.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     b= color.rgb.b
#     g=color.rgb.g
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

clr=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

screen = Screen()
screen.setup (width=520, height=520, startx=0, starty=0)
tim = t.Turtle()
tim.speed(0)
tim.penup()
tim.goto(-230,-230)
for j in range(0,500,50):
    for i in range(0,500,50):
        tim.dot(20,clr[random.randint(0,len(clr)-1)])
        tim.forward(50)
    tim.right(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen.exitonclick()