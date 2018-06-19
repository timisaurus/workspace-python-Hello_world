# This program calculates if a triangle with 3 different lenght would be possible.

x = int(input('Lenght a:'))
y = int(input('Lenght b:'))
z = int(input('Lenght c:'))


def is_triangle(a, b, c):
    ab = a + b
    ac = a + c
    bc = b + c
    result = True
    if bc < a:
        result = False
    if ac < b:
        result = False
    if ab < c:
        result = False
    if result == True:
        print('possible triangle')
    if result == False:
        print('inpossible triangle')
    x = int(input('Lenght a:'))
    y = int(input('Lenght b:'))
    z = int(input('Lenght c:'))
    is_triangle(x, y, z)


is_triangle(x, y, z)
