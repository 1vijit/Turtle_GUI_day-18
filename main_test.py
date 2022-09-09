# #####Turtle Intro######
#
# import turtle as t
# from turtle import Screen
#
# tim = t.Turtle()
# tim.shape("turtle")
# tim.color("red")
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     my_tuple = (r,g,b)
#     return my_tuple

######## Challenge 1&2 - Draw a Square ############
# tim.pensize(3)
#
# for _ in range(15):
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
#     tim.forward(5)
#
#
# screen = Screen()
# screen.exitonclick()

####### Challenge 3 - Draw shapes ############
# number = int(input("How many vertex points do you want? "))
#
# tim.pendown()
# r=10.0
# g=10.0
# b=10.0
# for x in range(3,number+1):
#     num = x
#     r+=10
#     b+=10
#     g+=10
#     angle = 360 / num
#     for i in range(num):
#         tim.forward(100)
#         tim.left(angle)


######## Challenge 4 - Random walk ############
#
# import random
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.pendown()
# clr_len = len(colours)
# tim.speed(0)
# for _ in range(50):
#     clr = random.randint(0,clr_len-1)
#     tim.color(random_color())
#     tim.width(5)
#     num1 = random.randint(0,60)
#     tim.forward(num1)
#     ang = random.choice([0,90,180,270])
#     tim.left(ang)
# screen = Screen()
# screen.exitonclick()

import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
tim.pendown()
tim.speed(0)
tim.width(5)
for i in range(0,360,10):
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(100)



screen = Screen()
screen.exitonclick()