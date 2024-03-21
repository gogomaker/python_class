import turtle

wn = turtle.Screen()
wn.bgcolor("light green")

t = turtle.Turtle()
t.shape("turtle")
t.color("pink")

t.penup()
size = 20

for i in range(50):
    t.stamp()
    size += 3
    t.forward(size)
    t.right(24)
    