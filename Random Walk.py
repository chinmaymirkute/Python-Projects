#welcome to Random Walk python code
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute
import turtle as t
import random

Chinmay = t.Turtle()
Chinmay.hideturtle()


colours = ["blue", "black", "red"]
directions = [0, 90, 180, 270, 360]
Chinmay.pensize(10)
Chinmay.speed("fastest")

for _ in range(1000):
    Chinmay.color(random.choice(colours))
    Chinmay.forward(30)
    Chinmay.setheading(random.choice(directions))
