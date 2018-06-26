'''
sorted list (ascending order)
'''


# A function that accepts a positive integers and returns a sorted list
# of all prime numbers between 2 and n (including 2 / excluding n).

def list_of_primes(n):
    output_list = []
    for element in range(2, n):
        current_devisor = 2
        is_current_number_prime = True
        while (current_devisor < element):
            if element % current_devisor == 0:
                is_current_number_prime = False
                break
            current_devisor = current_devisor + 1
        if is_current_number_prime:
            output_list.append(element)
    output_list.sort
    return (output_list)


print(list_of_primes(56))
'''

# A program to Determine if a number is prime
while True:
    current_number=prime?
    current_devisor=2
    is_current_number_prime=True
    while(current_devisor<current_number):
        if current_number%current_devisor==0:
            is_current_number_prime=False
            print(current_number, 'is no prime')
            break
        current_devisor=current_devisor+1
    if is_current_number_prime:
        print(current_number, 'is prime')
    print ('All done!')
'''
