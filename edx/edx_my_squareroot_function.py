# This function calculates monthly payment for a loan

def calculate_loan_payment(principal, annual_interest_rate, duration):
    principal = float(principal)
    annual_interest_rate = float(annual_interest_rate)
    duration = int(duration)
    total_monthly_payments = duration * 12
    if annual_interest_rate == 0:
        return principal / (duration * 12)
    total_monthly_payments = duration * 12
    monthly_interest_rate = annual_interest_rate / 100 / 12
    monthly_payment = principal * ((monthly_interest_rate * ((1 + monthly_interest_rate) **
                                                             total_monthly_payments)) / (
                                           ((1 + monthly_interest_rate) ** total_monthly_payments) - 1))
    return monthly_payment


calculate_loan_payment(1000.0, 4.5, 5)

'''
def function(vector):
    ax = vector[0]
    ay = vector[1]
    az = vector[2]
    a = (((ax * ax) + (ay * ay) + (az * az))**0.5)
    x = ax/a
    y = ay/a
    z = az/a
    new_list = [x, y, z]
    return new_list


def function(smaple_list):
    new_list = []
    for item in smaple_list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

x = [2, 5, 7, 8, 3]
print (function(x))


my_list = [1, 4, 7, 6, 8, 9]
def function(x):
    my_sum = 0
    for item in x:
        my_sum = my_sum+item
    return my_sum

print(function(my_list))


def function(sample_list):
    new_list = 0
    for item in sample_list:
        if item<new_list:
            new_list = item
    return new_list


# Tis function calculates and returnes the square root
# of the number which is given to in a input.

def my_square_root(input_number):
    square_root=input_number/2
    accuracy=0.001
    while abs(input_number-(square_root**2))>accuracy:
        square_root=(square_root+(input_number/square_root))/2
    return square_root

# This is the main program to check the my_square_root_function

for x in range(1,21):
    y=my_square_root(x)
    print('Square root of', x, 'is', y)
'''
