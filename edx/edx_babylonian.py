# This programm calculates the square root
# of a number

number_input = (input("Number: "))
number = float(number_input)
guess = number / 2
accuracy = 0.01
iteration = 0
while abs(number - (guess ** 2)) > accuracy:
    print('Iteration', iteration, 'Guessed square root is:', guess)
    guess = (guess + (number / guess)) / 2
    iteration = iteration + 1
print("Original number is: ", number)
print("Square root of a number is: ", guess)
