# This program calculates and prints loan information.

# This function lets the user input 3 times.
def input_user():
    x = float(input('principal :'))
    y = float(input('annual_interest_rate :'))
    z = int(input('duration :'))
    loan_information(x, y, z)


# This function calculates the main information.
def loan_information(principal, annual_interest_rate, duration):
    total_monthly_payments = duration * 12
    monthly_interest_rate = annual_interest_rate / 100 / 12
    if annual_interest_rate == 0:
        return principal / (duration * 12)
    monthly_payment = principal * ((monthly_interest_rate * ((1 + monthly_interest_rate) **
                                                             total_monthly_payments)) / (
                                           ((1 + monthly_interest_rate) ** total_monthly_payments) - 1))
    total_payment = monthly_payment * 12
    total_payment_loop = total_payment
    a = principal
    b = annual_interest_rate
    c = duration
    d = monthly_payment
    e = total_payment_loop
    f = total_payment
    output_loan_information(a, b, c, d, e, f)


# This function calculates the remaining balance.
def remaining_balance(a, b, c, d):
    n = c * 12
    r = b / 100 / 12
    if b == 0:
        return a - d * (a / n)
    rn1 = (1 + r) ** n
    rd1 = (1 + r) ** d
    balance = a * ((rn1 - rd1) / (rn1 - 1))
    return balance


# This function gives the output of the functions above.
def output_loan_information(principal, annual_interest_rate, duration, monthly_payment,
                            total_payment_loop, total_payment):
    print('LOAN AMOUNT:', int(principal), 'INTEREST RATE (PERCENT):', int(annual_interest_rate))
    print('DURATION (YEARS):', int(duration), 'MONTHLY PAYMENT:', int(monthly_payment))
    for years in range(duration):
        years = years + 1
        print('YEAR:', int(years), 'BALANCE:', int(remaining_balance(principal, annual_interest_rate,
                                                                     duration, years * 12)), 'TOTAL PAYMENT',
              int(total_payment_loop))
        total_payment_loop = total_payment_loop + total_payment


input_user()

'''
# This function returns the remaining loan balance.

def remaining_loan_balance(principal, annual_interest_rate, duration , number_of_payments):
    principal = float(principal)
    annual_interest_rate = float(annual_interest_rate)
    duration = int(duration)
    number_of_payments = int(number_of_payments)
    monthly_interest_rate = annual_interest_rate/100/12
    total_payments = duration*12
    if annual_interest_rate == 0:
        loan_balance = principle*(1-(number_of_payments/total_payments))
    else:
        rn1 = (1+monthly_interest_rate)**total_payments
        rp1 = (1+monthly_interest_rate)**number_of_payments
        loan_balance = principal*((rn1-rp1)/(rn1-1))
    return loan_balance
    
print(remaining_loan_balance(1000.0,4.5,5,12))


def calculate_loan_payment(principal, annual_interest_rate, duration):
    principal = float(principal)
    annual_interest_rate = float(annual_interest_rate)
    duration = int(duration)
    total_monthly_payments = duration*12
    if annual_interest_rate == 0:
        return principal/(duration*12)
    total_monthly_payments = duration*12
    monthly_interest_rate = annual_interest_rate/100/12
    monthly_payment = principal*((monthly_interest_rate*((1+monthly_interest_rate)**
    total_monthly_payments))/(((1+monthly_interest_rate)**total_monthly_payments)-1))
    return monthly_payment

calculate_loan_payment(1000.0,4.5,5)

'''
