#welcome to the Turtle Race
#coded by - Chinmay Mirkute
#you can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


#Please enter your selection in Lowercase letters

from turtle import Turtle, Screen
import random

Race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_selection = screen.textinput(title="Welcome to the Turtle Race", prompt="Enter your Selection (blue/red): ")
turtle_colors = ["red", "blue"]
y_positions = [-10, 20]
total_turtles = []


for the_turtles in range(0, 2):
    new_turtle = Turtle(shape="turtle")
    new_turtle.turtlesize(1)
    new_turtle.penup()
    new_turtle.color(turtle_colors[the_turtles])
    new_turtle.goto(x=-230, y=y_positions[the_turtles])
    total_turtles.append(new_turtle)

if user_selection:
    Race_on = True

while Race_on:
    for turtle in total_turtles:

        if turtle.xcor() > 230:
            Race_on = False
            winner = turtle.pencolor()
            if winner == user_selection:
                print(f"congratulations!!! You've won!")
            else:
                print(f"Hard Luck! You've lose , Try again")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()