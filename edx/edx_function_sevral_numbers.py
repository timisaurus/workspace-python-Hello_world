# A function that accepts two lists containing integers.
# It returns the sum of all even numbers.

def all_even_numbers(input_list_a, input_list_b):
    output = 0
    for element in input_list_a:
        if element % 2 == 0:
            output += element
    for element in input_list_b:
        if element % 2 == 0:
            output += element
    return output


file = open("test_file.txt", "r")
print(len(str(file)))
print(file.read(11))
file.close()

# A program that prints a triangle from 1 to the user_input.

user_input = int(input('Enter Number: '))
triangle_builder = 1
while triangle_builder <= user_input:
    print(str(triangle_builder) * triangle_builder)
    triangle_builder += 1

# A program that prints a asterisks square with the dimensions
# of the user_input.

user_input = int(input('Enter Number: '))
asterisks_builder = 1
for element in range(user_input):
    print('*' * user_input)
    asterisks_builder += 1

# A program that prints a downward triangle
# out of asterisks from the user input.

user_input = int(input('Enter Number: '))
print('*' * user_input)
user_input -= 1
while 0 < user_input:
    space_count = 0
    if user_input - 2 > 0:
        space_count = user_input - 2
    if space_count > 0:
        print('*', ' ' * space_count, '*', sep='')
    else:
        print('*' * user_input)
    user_input -= 1
