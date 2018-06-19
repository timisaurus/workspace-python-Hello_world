"""
def cursed():
    cursed()

devisable_numbers=0
number=1
while number<101:
    if number%5 == 0:
        devisable_numbers = devisable_numbers+number
        number = number+1
    else:
        number = number+1
print (devisable_numbers)

n = int(input())
factorial_number = 1
number = 1
while number <= n:
    factorial_number = factorial_number * number
    number = number + 1
print(factorial_number)


n = int(input())
number = n-1
factorial_number = number*n
while number != 1:
    number = number-1
    factorial_number = factorial_number*number
print (factorial_number)

"""
factorial_number = 0
number = 1
while number < 1002:
    factorial_number = factorial_number + number
    number = number + 3
print(factorial_number)
