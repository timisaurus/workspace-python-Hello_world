'''
# This program prints every character
# of the string

for character in 'computer':
    print(character)

print('Finished the for loop \n')

# This program shows the use of continue
# statement in a for loop

for character in 'computer':
    if character == 'p':
        continue
    print(character)

print('Finished the for loop with a continue\n')

# This programm shows the use of break
# statements in a for loop

for character in 'computer':
    if character == 'p':
        break
    print(character)

print('Finished the for loop with a break')

'''

count = 20
for x in range(0, 10):
    count = count - 1
    if x == 2:
        break

print(count)
