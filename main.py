import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("peru")
turtle_directions = [0, 90, 180, 270]


def turtle_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def rand_walk():
    tim.pensize(15)
    tim.speed("fast")
    for _ in range(30):
        tim.color(turtle_random_color())
        direction = choice(turtle_directions)
        tim.right(direction)
        tim.forward(50)

def draw_shape(num_sides):
    angle = 360
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle / num_sides)


def drawing_shapes():
    for i in range(3, 11):
        tim.color(turtle_random_color())
        draw_shape(i)

def draw_spirograph(size_of_gap):
    tim.pensize(3)
    tim.speed("fastest")
    for i in range (int(360 / size_of_gap)):
        tim.color(turtle_random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


# drawing_shapes()
# rand_walk()

draw_spirograph(5)
screen = Screen()
screen.exitonclick()
