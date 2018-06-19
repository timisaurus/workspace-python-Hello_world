import math
import turtle

t = turtle.Turtle()
print(t)


def polygon(turtle, length, n):
    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for x in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


def polyline(t, n, lenght, angle):
    for x in range(n):
        t.fd(length)
        t.lt(angle)


arc(t, 50, 150)

'''
t = turtle.Turtle()
print(t)

def polygon(turtle, length, n):
    angle = 360 / n
    for x in range(n):
        t.fd(length)
        t.lt(angle)

def circle(turtle, r):
    circumference = 2 *math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(turtle, length, n)

circle(turtle=t , r=120)

def square(t, length):
    tim = turtle.Turtle()
    print(tim)
    for X in range(9):
        tim.pd()
        tim.fd(length)
        tim.lt(20)
        tim.pu()
        tim.fd(length)
        tim.lt(20)

        
    turtle.mainloop()
    


square('running', 50)


def polygon(t, length, n):
    tim = turtle.Turtle()
    print(tim)
    for X in range(9):
        tim.pd()
        tim.fd(length)
        tim.lt(n)
        tim.pu()
        tim.fd(length)
        tim.lt(n)
    turtle.mainloop()

def circle(t, r):
    jeff = turtle.Turtle()
    print(jeff)
    for X in range(140):
        jeff.fd(t)
        jeff.lt(r)
    turtle.mainloop()

def arc(t, r, angle):
    jeff = turtle.Turtle()
    print(jeff)
    for X in range(angle):
        jeff.fd(t)
        jeff.lt(r)
    for X in range(115-angle):
        jeff.pu()
        jeff.fd(t)
        jeff.lt(r)
    turtle.mainloop()

def polytwo(x_turtle, n, lenght, repeats):
    x_turtle = turtle.Turtle()
    angle = 360.0/n
    print(x_turtle)
    for y in range(repeats):
        x_turtle.fd(lenght)
        x_turtle.lt(angle)
    turtle.mainloop()

    
polytwo("jeff" , 3.14, 100, 22)
polygon('running', 50, 20)

'''
