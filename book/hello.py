import math

'''
a = 15/60
b = 12/60
c = (8+a)*2
d = (7+b)*3
e = (c+d)/60
f = 52/60
g = f+e
h = g+6
i = int (h)
j = (h-i)*60/100
k = j+i
print (k)

#BitwiseOperators
a = 50
b = 25
c = a & b
d = a << 2
e = a ^ b
f = ~a
g = ~f
print (c)
print (d)
print (e)
print (f)
print (g)

#List
a = ["Zero", "Student", "Warrior", "Hero", "Teacher"]
print (a)
print (a[0])
print (a[:2])

print("print shows things")

#Variables
a = 2
b = 6
print (a+b)

#Add two numbers 
sum = a+b
print (sum)
'''

# Strings
a = "1"
b = "2"
print(a + b)

# Add two numbers 2
sum = a + b
print(sum)

# print ("i am a comment")
print("Not a comment")

# :, enter & tap needed for action
a = "sample text"
b = "sample text"
c = "sample text 2"
if a == b:
    print("string a & b equal")
if a != c:
    print("string a & c not equal")

# self explanatory (͡°͜ʖ͡°)
a = "excites"
print(a)
print(a[6])
print(a[0])
print(a[1])

# called startindex:pastindex
a = "get over it"
print(a[4:8])
print(a[4:])
print(a[:8])

# integer = 1,2,3,4
# float = 0.1234 (numbers behind dot)
# boolean = True or False

a = 12
b = 0.12
c = "True"

print(a, b, c)

# int and str casting
a = "1"
b = 8
print(int(a) + b)
print(str(b) + a)

# Math 101
print("The Big Math")
A = 2
B = 3

print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A % B)
print(A ** B)
print()
print(abs(A + B))
print(pow(A, B))
print()
# import math used for math.
print(math.sqrt(A + B))
print(math.exp(A))
print(math.log(A))
print(math.log10(A))
print(math.gamma(A))

# calculator?
a = int(input("add:"))
b = int(input("to:"))

sum = a + b
print("sum:")
print(sum)

# username = string / input("sample text") = input someting, to code below
username = input("Username:")
print(username)

# above = the same in phyton v 2.X and under:
# input = raw_input
