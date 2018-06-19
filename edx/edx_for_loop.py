'''
for iteration_variable in sequence:
    statement(s)
print('not inside while')

number_of_books = 0
my_books = ['phyton', 'java', 'c++', 'Ruby']
for current_book in my_books:
    number_of_books = number_of_books+1
    print('Nr.', number_of_books, 'Book:', current_book)
print('No more books on my shelf')

for current_number in range (1,101) :
    print('iteration', current_number, 'hallo')
'''
add_number = 0
number_sum = 0
for current_number in range(1, 101):
    if current_number % 2 == 0:
        add_number = add_number + 2
        number_sum = number_sum + add_number
print(number_sum)
'''
n = int(input())

add_number = 0
number_sum = 0
for n in range (1,n+1) :
    add_number = add_number+1
    op_number = add_number**2
    number_sum = number_sum+op_number
print(number_sum)

n = int(input())

number_sum = 1
for n in range (1,n+2) :
    print(number_sum)
    number_sum = number_sum*10
'''
