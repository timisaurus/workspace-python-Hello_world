# A function that accepts a list as parameter and returns
# the greatest common divisor.

def find_gcd(some_list):
    gcd = 1
    iterator = 2
    some_list.sort()
    smallest_int = some_list[0]
    while 0 < smallest_int:
        element_iteration = True
        for elements in some_list:
            if elements % iterator != 0:
                element_iteration = False
        if element_iteration:
            gcd = iterator
        iterator += 1
        smallest_int -= 1
    return gcd
