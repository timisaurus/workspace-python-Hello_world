# A program to Determine if a number is prime
while True:
    current_number = int(input('a number: '))
    current_devisor = 2
    is_current_number_prime = True
    while (current_devisor < current_number):
        if current_number % current_devisor == 0:
            is_current_number_prime = False
            print(current_number, 'is no prime')
            break
        current_devisor = current_devisor + 1
    if is_current_number_prime:
        print(current_number, 'is prime')
    print('All done!')

"""
m = 0
for x in range (1,3):
    for y in range (4,6):
        print ('x = ', x)
        print ('y = ', y)
        m = m + x + y
        print (m)

m = 0
for x in range (1,3):
    k = 0
    for y in range (-2,0):
        print ('x = ', x)
        print ('y = ', y)
        k = k + y
        m = m + k
        print (k)
        print (m)

m = 0
for x in [3,5,3]:
    for y in range (10,11):
        print(x)
        print(y)
        m = m + x + y
        print (m)
'''

m = 0
x = 1
while x < 4:
    y = 1
    while y < 1:
        m = m + x + y
        y = y + 1
    x = x + 1
print(m)
"""
