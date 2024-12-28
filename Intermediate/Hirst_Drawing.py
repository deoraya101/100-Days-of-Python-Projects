import turtle as t
import random
import colorgram


tim = t.Turtle()
t.colormode(255)

color_list = []
colors = colorgram.extract('image.jpg', 20)
for i in colors:
    color_list.append(i.rgb[:])

def rand_color():
    color = random.choice(color_list)
    return color

tim.speed("fastest")

x = -300
y = -250

tim.penup()
tim.setposition(x, y)

def hirst_drawing():
    for i in range(10):
        tim.dot(20, rand_color())
        tim.penup()
        tim.forward(50)
    global y
    y += 50
    tim.setposition(x, y)

for _ in range(10):
    hirst_drawing()


screen = t.Screen()
screen.screensize(100, 100)
screen.exitonclick()
