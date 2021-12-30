#welcome to the Shapes Creator using python turtle module
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


import turtle as t
import random

Chinmay = t.Turtle()
Chinmay.pensize(5)
Chinmay.shape("turtle")
Chinmay.turtlesize(2)


colours = ["red", "Green", "Blue", "Orange", "Black", "Brown", "yellow", "pink","indigo","purple" ]

def the_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        Chinmay.forward(100)
        Chinmay.right(angle)

for shape_side_n in range(3, 10):
    Chinmay.color(random.choice(colours))
    the_shapes(shape_side_n)