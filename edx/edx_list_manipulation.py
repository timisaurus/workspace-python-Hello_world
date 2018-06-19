# This program accepts a integer between 1 to 9999 as parameter and returns
# the number as a string.

input_retry = True

n = 0
while input_retry:
    input_retry = False
    try:
        n = int(input('please enter an integer between 1 and 9999: '))
        assert n > 0 or n < 10000 == True
    except (AssertionError, TypeError, ValueError):
        print('Invalid input!')
        input_retry = True

int_fuck_me_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
str_fuck_me_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
                    'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                    'ninety', 'hundred', 'thousand']
comprehensive_double_digit_list = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                                   'seventy', 'eighty', 'ninety']
comprehensive_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

quadruple_output = ''
triple_output = ''
double_output = ''
single_output = ''
hundred_output = ''
thousand_output = ''
space_1 = ''
space_2 = ''
space_3 = ''
space_4 = ''
space_5 = ''
overcomplicated_not_space_5 = False
mass = 0
user_input = n

if user_input <= 9:
    while mass <= 10:
        if user_input == mass:
            single_output = comprehensive_list[mass - 1]
            break
        else:
            mass = mass + 1
elif user_input <= 99:
    double_digit_mass = 100
    while double_digit_mass >= 20:
        if user_input >= double_digit_mass:
            insert_double = int(double_digit_mass / 10 - 1)
            insert_single = user_input - double_digit_mass - 1
            double_output = comprehensive_double_digit_list[insert_double]
            single_output = comprehensive_list[insert_single]
            break
        else:
            double_digit_mass = double_digit_mass - 10
elif user_input <= 9999:
    x = user_input
    quadruple_digit_mass = 10000
    while quadruple_digit_mass >= 1000:
        if x >= quadruple_digit_mass:
            insert_quadruple = int(quadruple_digit_mass / 1000 - 1)
            quadruple_output = comprehensive_list[insert_quadruple]
            thousand_output = 'thousand'
            x = x - quadruple_digit_mass
        else:
            quadruple_digit_mass = quadruple_digit_mass - 1000
    triple_digit_mass = 1000
    while triple_digit_mass >= 100:
        if x >= triple_digit_mass:
            insert_triple = int(triple_digit_mass / 100 - 1)
            triple_output = comprehensive_list[insert_triple]
            hundred_output = 'hundred'
            x = x - triple_digit_mass
        else:
            triple_digit_mass = triple_digit_mass - 100

    if x == 0:
        pass
    elif x <= 9:
        test = user_input - 1
        if test < 10000:
            if test < 1000:
                space_4 = ''
                space_5 = ' '
            else:
                space_2 = ''
                space_3 = ''
                space_4 = ''
                space_5 = ' '
        insert_single = x - 1
        single_output = comprehensive_list[insert_single]
        pass

    elif x <= 99:
        double_digit_mass = 100
        while double_digit_mass >= 20:
            if x >= double_digit_mass:
                insert_double = int(double_digit_mass / 10 - 1)
                insert_single = x - double_digit_mass - 1
                double_output = comprehensive_double_digit_list[insert_double]
                if insert_single == -1:
                    single_output = ''
                else:
                    single_output = comprehensive_list[insert_single]
                break
            else:
                double_digit_mass = double_digit_mass - 10

        mass = 0
        for int_elements in int_fuck_me_list:
            if x == int_elements:
                while mass <= 20:
                    if int_elements == int_fuck_me_list[mass]:
                        double_output = str_fuck_me_list[mass]
                        single_output = ''
                        overcomplicated_not_space_5 = True
                        break
                    else:
                        mass += 1
                break

mass = 0
for int_elements in int_fuck_me_list:
    if user_input == int_elements:
        while mass <= 20:
            if int_elements == int_fuck_me_list[mass]:
                double_output = str_fuck_me_list[mass]
                single_output = ''
                overcomplicated_not_space_5 = True
                break
            else:
                mass += 1
        break

if quadruple_output != '':
    space_1 = ' '
if triple_output != '':
    space_2 = ' '
    space_3 = ' '
if double_output != '':
    space_4 = ' '
    if not overcomplicated_not_space_5:
        space_5 = ' '
if user_input < 1000:
    space_2 = ''
if user_input < 100:
    space_4 = ''

print(quadruple_output, space_1, thousand_output, space_2, triple_output, space_3,
      hundred_output, space_4, double_output, space_5, single_output, sep='')
