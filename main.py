import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed(0)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
def randome_color():
    return random.choice(color_list)

for y in range(-250, 250, 50):
        for x in range(-250, 250, 50):
            tim.goto(x, y)
            tim.dot(20,randome_color())

screen = t.Screen()
screen.exitonclick()