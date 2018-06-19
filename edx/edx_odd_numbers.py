# This function returns the number of chicken and dogs.
def animal_amount(heads, legs):
    amount_dog = 0
    if legs % 2 == 0:
        if heads + 3 < legs:
            if legs > 5 and heads > 1:
                amount_chicken = legs // 2
                if amount_chicken > heads:
                    while amount_chicken > 0:
                        amount_chicken = amount_chicken - 2
                        amount_dog = amount_dog + 1
                        amount_dog_chicken = amount_dog + amount_chicken
                        animal_list = [amount_chicken, amount_dog]
                        if amount_dog_chicken == heads:
                            return animal_list
                        if amount_chicken < 1:
                            return None
                    return True
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None


# This function returns the least common multiple of to parameters.
def find_lcm(a, b):
    test_number = 1
    while True:
        if test_number % a == 0:
            if test_number % b == 0:
                return test_number
        test_number = test_number + 1


# A function to return if a number is prime
def is_this_prime(n):
    if n == 2:
        return True
    if n == 0:
        return False
    if n == 1:
        return False
    for number in range(3, n):
        if n % number == 0:
            return False
    return True


# This function test if the parameter is a perfect number.
def perfect_number(positive_integer):
    devisors = 0
    for numbers in range(1, positive_integer):
        if positive_integer % numbers == 0:
            devisors = devisors + numbers
    if devisors == positive_integer:
        return True
    else:
        return False


# This function returns all odd numbers in a list which get added together.
def odd_numbers(user_list):
    sum_odd_numbers = 0
    for integer in user_list:
        if integer % 2 == 0:
            pass
        else:
            sum_odd_numbers = sum_odd_numbers + integer
    return sum_odd_numbers
