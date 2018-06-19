n = int(input())


def pyramid(n):
    t = n
    star = '*'
    additional_star = '*'
    while 0 < n:
        print(star)
        star = star + additional_star
        n = n - 1
    star = star.replace('*', '', 1)
    for char in star:
        star = star.replace('*', '', 1)
        print(star)


pyramid(n)

'''
my_list = ["pet" ,"dog", 35, "cat", 23]
count = 0
for item in my_list:
    if type(item)== str:
        continue
    count = count + 1
print(count)

def average_list(user_list):
    list_max = user_list[0]    
    for integer in user_list:
        if integer >= list_max:
            list_max = integer
    return list_max

def average_list(user_list):
    list_sum = 0
    for integer in user_list:
        list_sum =list_sum+integer
    number_of_items=len(user_list)
    list_sum = list_sum/number_of_items
    return list_sum
    
def rectangle(height,width):
    area=height*width
    perimeter=(height*2)+(width*2)
    return [area,perimeter]

from math import cos, sqrt
def MATICMONSTER(a, b):
    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]
    distance=sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
    return distance

f = [2, 3, -5]
g = [4,-3, 12]
print(MATICMONSTER(g, f))
'''
