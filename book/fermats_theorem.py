# This program tries to disprove the fermates theorem

def it_worked():
    print('Holy smokes, Fermat was wrong!')
    user_input = int(input('type a positive integer again: '))

    a = user_input
    b = user_input
    c = user_input
    n = user_input

    ticker(a, b, c, n)


def it_didnt_worke():
    print('No, that doesnt work.')
    user_input = int(input('type a positive integer again: '))

    a = user_input
    b = user_input
    c = user_input
    n = user_input

    ticker(a, b, c, n)


def check_fermat(a, b, c, n):
    sum_c = (a ** n) + (b ** n)
    if (a ** n) + (b ** n) == (c ** n):
        it_worked()


def ticker(a, b, c, n):
    x = a
    z = b
    y = c
    w = n

    e = a
    f = b
    g = c
    o = n

    while a > 1:
        a = a - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while b > 1:
        b = b - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while c > 1:
        c = c - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    a = x
    b = y
    c = z
    while a > 1:
        a = a - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while c > 1:
        c = c - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while b > 1:
        b = b - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    a = x
    b = y
    c = z

    while b > 1:
        b = b - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while c > 1:
        c = c - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while a > 1:
        a = a - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    a = x
    b = y
    c = z
    while b > 1:
        b = b - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while a > 1:
        a = a - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while c > 1:
        c = c - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    a = x
    b = y
    c = z

    while c > 1:
        c = c - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while b > 1:
        b = b - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while a > 1:
        a = a - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    a = x
    b = y
    c = z
    while c > 1:
        c = c - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while a > 1:
        a = a - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)
    while b > 1:
        b = b - 1
        check_fermat(a, b, c, n)
        print(a, b, c, n)

    if a == 1 and b == 1 and c == 1 and n == 2:
        it_didnt_worke()

    if a == 1 and b == 1 and c == 1:
        n = n - 1
        a = e
        b = f
        c = g
        e = e - 1
        f = f - 1
        g = g - 1
        o = o - 1
        ticker(e, f, g, o)


user_input = int(input('type a positive integer: '))

a = user_input
b = user_input
c = user_input
n = user_input

ticker(a, b, c, n)
