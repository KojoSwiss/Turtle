import turtle as t
import random
from turtle import Screen

t.colormode(255)
benny = t.Turtle()
benny.shape("turtle")
benny.color("DarkOrange2")


# colors = ["SeaGreen1", "tomato1", "SkyBlue3", "sienna", "RosyBrown3", "SeaGreen4"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# for i in range(4):
#     benny.forward(100)
#     benny.right(90)


# def draw_shape(n_sides):
#     angle = 360 / n_sides
#     for i in range(n_sides):
#         benny.forward(50)
#         benny.right(angle)
#
#
# for x in range(3, 11):
#     benny.color(random.choice(colors))
#     draw_shape(x)
#
# directions = [0, 90, 180, 270]
benny.speed("fastest")


# for x in range(200):
#     benny.width(15)
#     benny.color(random_color())
#     benny.forward(20)
#     benny.setheading(random.choice(directions))

def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        benny.color(random_color())
        benny.circle(100)
        benny.setheading(benny.heading() + gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
