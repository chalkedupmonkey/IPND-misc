# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle


def draw_square(aturtle):

        for index in range(4):
            aturtle.forward(100)
            aturtle.right(90)



def draw():
    window = turtle.Screen()
    window.bgcolor('blue')
    jeff = turtle.Turtle()
    jeff.shape('turtle')
    jeff.color('white')
    jeff.speed(20)
    for index in range(36):
        draw_square(jeff)
        jeff.right(10)



    window.exitonclick()



draw()
