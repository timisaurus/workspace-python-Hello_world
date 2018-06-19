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
