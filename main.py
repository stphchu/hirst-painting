# import colorgram
import random
from turtle import Turtle, Screen

# extracted_colors = colorgram.extract("./image.jpg", 50)
# color_palette = []
#
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     color_palette.append(rgb_color)

color_list = [(212, 154, 98), (53, 107, 132), (174, 78, 36), (199, 142, 34), (117, 155, 171),
              (125, 79, 98), (123, 175, 157), (227, 198, 129), (190, 88, 109), (55, 38, 20),
              (12, 50, 65), (200, 124, 140), (43, 168, 128), (53, 125, 119), (165, 21, 30),
              (223, 93, 78), (243, 163, 160), (4, 25, 24), (38, 32, 34), (80, 147, 169), (163, 26, 21),
              (181, 206, 183), (20, 80, 92), (234, 165, 170), (103, 126, 158), (164, 203, 211),
              (16, 103, 97), (60, 61, 73), (82, 68, 39), (183, 190, 204)]

brush = Turtle()
screen = Screen()
screen.colormode(255)
brush.speed("fastest")
brush.ht()

def reset_pos(y):
    brush.pu()
    brush.setpos(-250, y)


num_dots = 0
y = -200
while num_dots < 100:
    reset_pos(y)
    for _ in range(11):
        brush.dot(20, random.choice(color_list))
        num_dots += 1
        brush.fd(50)
    y += 50

screen.exitonclick()