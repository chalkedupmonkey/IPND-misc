# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

window = turtle.Screen()
window.bgcolor("blue")
window.exitonclick()

def draw_square():

    jeff = turtle.Turtle()
    jeff.shape("turtle")
    jeff.color("white")

    for index in range(3):
        jeff.forward(100)
        jeff.right(90)


def draw_circle():

    jemmie = turtle.Turtle()
    jemmie.shape("turtle")
    jemmie.color("purple")
    jemmie.circle(100)



def draw_triangle():

    thien = turtle.Turtle()
    thien.shape("turtle")
    thien.color("red")

    thien.left(180)

    for index in range(2):
        thien.forward(100)
        thien.left(120)

    thien.right(60)



draw_square()
draw_circle()
draw_triangle()
