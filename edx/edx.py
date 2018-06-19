x = ['123', 1, 'asd']
print(x)

# This program converts from Celsius to Fahrenheit
celsius = float(input("convert celsius:"))

Fahrenheit = (((celsius * 9) / 5) + 32)


def result_comment():
    if Fahrenheit < 30:
        print(int(Fahrenheit), 'degrees Fahrenheit, freezing cold')
    elif Fahrenheit < 50:
        print(int(Fahrenheit), 'degrees Fahrenheit, chilly')
    elif Fahrenheit < 90:
        print(int(Fahrenheit), 'degrees Fahrenheit, OK')
    else:
        print(int(Fahrenheit), 'degrees Fahrenheit, Hot')


result_comment()

'''
# This program checks if answer is devidable by 0
answer = int(input())
if answer % 3 == 0:
    print("Yes")
else:
    print("No")

answer = str(input())
if "dog" in answer:
    print('Yes')
else:
    print('No')

if expression:
    statement(s)
else:
    statement(s)

print ('not inside if')


list_x = [6, 'cat', 'dog', 4.5]

def list_search():
    user_search = input('Search List: ')

    if user_search in list_x:
        print(True)
    if user_search not in list_x:
        print(False)

list_search()

'''
'''

# This program converts from Celsius to Fahrenheit
celsius = float(input("convert celsius:"))

Fahrenheit = (((celsius*9)/5)+32)

def result_comment(): 
    if Fahrenheit >= 90:
        print (int(Fahrenheit), 'degrees hot in Fahrenheit')
    else:
        if Fahrenheit == 1 or 0:
            print (int(Fahrenheit), 'degree cold in Fahrenheit')
        else:
            print (int(Fahrenheit), 'degrees cold in Fahrenheit')
            
result_comment()

'''
'''
hight=20
width=30
area=2*(hight*width)
perimeter=2*(hight*width)        
print (hight)
print (width)


user_interaction=input()
print (user_interaction)


my_list = [int, float]

print(my_list)



# Type your code here

user_age_years = int(input('your age: '))

user_age_days = user_age_years*365

print('You are', user_age_days, 'days old')


import math

x = float(input())
y = (math.sqrt(x)) - (12*x) + 11
print (y)

# Type your code here

list_weekday = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

user_weekday = int(input())
user_weekday_index = user_weekday-1

print(list_weekday[user_weekday_index])

# Type your code here
sample_list = [2, 10, 3, 5]
sample_list_added_together = sample_list[0]+sample_list[1]+sample_list[2]+sample_list[3]
sample_list_average = sample_list_added_together/4

print(sample_list_average)
'''
