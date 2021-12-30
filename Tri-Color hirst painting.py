#welcome to Tri-Color hirst painting python code
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute

import turtle as t
import random

t.colormode(255)
Chinmay = t.Turtle()
Chinmay.speed("fastest")
Chinmay.penup()
Chinmay.shape("turtle")
Chinmay.turtlesize(2)

color_list = ["blue", "black", "red"]
Chinmay.setheading(225)
Chinmay.forward(300)
Chinmay.setheading(0)
total_dots = 101

for the_counts in range(1, total_dots):
    Chinmay.dot(20, random.choice(color_list))
    Chinmay.forward(50)

    if the_counts % 10 == 0:
        Chinmay.setheading(90)
        Chinmay.forward(50)
        Chinmay.setheading(180)
        Chinmay.forward(500)
        Chinmay.setheading(0)









screen = t.Screen()
screen.exitonclick()