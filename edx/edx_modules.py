# Program to test modules
import math

from edx_tim_math import add_numbers, \
    multiply_numbers  # instead of functions themselfs you can just time * for all functions

a = 5
b = 8
c = add_numbers(a, b)
print(c)
d = multiply_numbers(a, b)
print(d)
print(math.sqrt(4))

'''
import edx_tim_math

a=5
b=8
c=edx_tim_math.add_numbers(a,b)
print (c)
d=edx_tim_math.multiply_numbers(a,b)
print (d)
'''
