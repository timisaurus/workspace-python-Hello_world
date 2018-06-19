# This program accepts a integer between 1 to 9999 as parameter and returns
# the number as a string.

n = int(input('please enter an integer between 1 and 9999: '))
int_fuck_me_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
str_fuck_me_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
                    'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                    'ninety', 'hundred', 'thousand']
comprehensive_double_digit_list = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
                                   'seventy', 'eighty', 'ninety']
comprehensive_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

quadruple_output = ''
triple_output = ''
double_output = ''
single_output = ''
hundred_output = ''
thousand_output = ''

# Fehlerhaft ab hier
if n <= 9:
    while mass <= 20:
        if n == mass:
            output = comprehensive_list[mass - 1]
            break
        else:
            mass = mass + 1
elif n <= 99:
    double_digit_mass = 100
    while double_digit_mass >= 20:
        if n >= double_digit_mass:
            insert_double = int(double_digit_mass / 10 - 2)
            insert_single = n - double_digit_mass - 1
            double_output = comprehensive_double_digit_list[insert_double]
            single_output = comprehensive_list[insert_single]
            break
        else:
            double_digit_mass = double_digit_mass - 10

# dangerous downwards
elif n <= 999:
    triple_digit_mass = 1000
    while triple_digit_mass >= 100:
        if n >= triple_digit_mass:
            insert_triple = int(triple_digit_mass / 100 - 1)
            n = n - triple_digit_mass
            double_digit_mass = 100
            while double_digit_mass >= 20:
                if n >= double_digit_mass:
                    insert_double = int(double_digit_mass / 10 - 2)
                    insert_single = n - double_digit_mass - 1
                    triple_output = comprehensive_list[insert_triple]
                    double_output = comprehensive_double_digit_list[insert_double]
                    single_output = comprehensive_list[insert_single]
                    break
                else:
                    double_digit_mass = double_digit_mass - 10
        else:
            triple_digit_mass = triple_digit_mass - 100
    # insert code
    # make them thair own function and return result(maybe)
    # or simply move up like under9999 under999 under99
# elif n<=9999:
#    pass    
# break
# dangerous upwards
# ab hier richtig
mass = 0
for int_elements in int_fuck_me_list:
    if n == int_elements:
        while mass <= 20:
            if int_elements == int_fuck_me_list[mass]:
                quadruple_output = ''
                triple_output = ''
                double_output = ''
                single_output = str_fuck_me_list[mass]
                break
            else:
                mass = mass + 1
        break
print(quadruple_output, thousand_output, triple_output, hundred_output, double_output, single_output)
'''
#This function accepts a list as parameter and returns a reverses it.
def traversing_backwards(input_list):
    output_list=[]
    while len(input_list)>0:
        output_list.append(input_list.pop(-1))
    return output_list

# This function accepts two lists as parameter and returns a list with unique elements only.
# Elements who only appear once are unique.
def extract_unique_elements_2_lists(input_list_a, input_list_b):
    output_list=[input_list_a.pop(0)]
    counter=0
    for input_element_a in input_list_a:
        for output_element in output_list:
            if output_element!=input_element_a:
                append_question=True
            else:
                append_question=False
                break
        if append_question==True:
            output_list.append(input_element_a)
        else:
            pass
    counter=0
    for input_element_b in input_list_b:
        for output_element in output_list:
            if output_element!=input_element_b:
                append_question=True
            else:
                append_question=False
                break
        if append_question==True:
            output_list.append(input_element_b)
        else:
            pass
    return output_list
'''
