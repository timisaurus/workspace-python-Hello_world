# This program draws the koch curve

import turtle

turtle.Turtle()


def koch(t, length_y):
    length_x = length_y / 3
    if length_y < 3:
        t.fd(length_y)
        koch(t, length_y)
    else:
        t.fd(length_x)
        t.lt(60)
        t.fd(length_x)
        t.rt(120)
        t.fd(length_x)
        t.lt(60)
        t.fd(length_x)


def koch_2(t, length_y):
    if length_y < 3:
        t.fd(length_y)
        koch(t, length_y)
    else:
        koch(t, length_y)
        t.lt(60)
        koch(t, length_y)
        t.rt(120)
        koch(t, length_y)
        t.lt(60)
        koch(t, length_y)
    return


def koch_3(t, length_z):
    if length_z < 3:
        t.fd(length_z)
        koch(t, length_z)
    else:
        koch_2(t, length_z)
        t.lt(60)
        koch_2(t, length_z)
        t.rt(120)
        koch_2(t, length_z)
        t.lt(60)
        koch_2(t, length_z)
    return


def koch_4(t, length):
    if length < 3:
        t.fd(length)
        koch(t, length)
    else:
        koch_3(t, length)
        t.lt(60)
        koch_3(t, length)
        t.rt(120)
        koch_3(t, length)
        t.lt(60)
        koch_3(t, length)
    return


def snowflake(t, length):
    if length < 3:
        t.fd(length)
        koch(t, length)
    else:
        koch_4(t, length)
        t.lt(60)
        koch_4(t, length)
        t.rt(120)
        koch_4(t, length)
        t.lt(60)
        koch_4(t, length)
    return


snowflake(turtle, 10)
