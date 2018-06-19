# This function accepts a list as parameter and returns a list with unique elements only.
# Elements who only appear once in a list are unique.
def extract_unique_elements(input_list):
    output_list = [input_list.pop(0)]
    counter = 0
    for input_element in input_list:
        for output_element in output_list:
            if output_element != input_element:
                append_question = True
            else:
                append_question = False
                break
        if append_question == True:
            output_list.append(input_element)
        else:
            pass
    counter = 0
    return output_list


# This function accepts two lists and returns the sum of all the odd integers.
def sum_odd_int(input_list_a, input_list_b):
    lenght_list_a = len(input_list_a)
    lenght_list_b = len(input_list_b)
    output_odd_int = 0
    if lenght_list_a >= lenght_list_b:
        for element_a in input_list_a:
            if len(input_list_b) > 0:
                element_b_use = input_list_b.pop(0)
                if element_b_use % 2 == 0:
                    pass
                else:
                    output_odd_int += element_b_use
            if element_a % 2 == 0:
                pass
            else:
                output_odd_int += element_a
    else:
        for element_b in input_list_b:
            if len(input_list_a) > 0:
                element_a_use = input_list_a.pop(0)
                if element_a_use % 2 == 0:
                    pass
                else:
                    output_odd_int += element_a_use
            if element_b % 2 == 0:
                pass
            else:
                output_odd_int += element_b
    return output_odd_int


# This function rounds up all odd numbers from a list and returns the list.
def round_up_odd_numbers(input_list):
    output_list = []
    for element in input_list:
        if element % 2 == 0:
            output_list.append(element)
        else:
            appendable_element = element + 1
            output_list.append(appendable_element)
    return output_list


# This function accepts a list as parameter
# and returns it without the first and last element.
def cut_list(input_list):
    input_list.pop(0)
    input_list.pop(-1)
    return input_list


# This function counts and returns how many time an element appears in a list.
def count_element_list(input_list, input_element):
    element_count = 0
    for_loop_count = 0
    for element in input_list[:]:
        if input_list[for_loop_count] == input_element:
            element_count = element_count + 1
        for_loop_count = for_loop_count + 1
    return element_count


# This function combines and sorts two lists and returns one list.
def combine_and_sort(input_list_a, input_list_b):
    for element in input_list_b[:]:
        element_x = input_list_b.pop(0)
        input_list_a.insert(-1, element_x)
    output_list = input_list_a
    count = len(output_list)
    smaller_integer = 0
    bigger_integer = 1
    for index in (output_list[:] * count):
        if output_list[smaller_integer] < output_list[bigger_integer]:
            element_a = output_list.pop(bigger_integer)
            element_b = output_list.pop(smaller_integer)
            output_list.insert(bigger_integer, element_b)
            output_list.insert(smaller_integer, element_a)
        smaller_integer = smaller_integer + 1
        bigger_integer = smaller_integer + 1
        if bigger_integer == count:
            smaller_integer = 0
            bigger_integer = 1
    return output_list


# This function returns a sorted list.
def sort_list(input_list):
    output_list = input_list
    count = len(output_list)
    smaller_integer = 0
    bigger_integer = 1
    for index in (output_list * count):
        if output_list[smaller_integer] > output_list[bigger_integer]:
            element_a = output_list.pop(bigger_integer)
            element_b = output_list.pop(smaller_integer)
            output_list.insert(bigger_integer, element_b)
            output_list.insert(smaller_integer, element_a)
        smaller_integer = smaller_integer + 1
        bigger_integer = smaller_integer + 1
        if bigger_integer == count:
            smaller_integer = 0
            bigger_integer = 1
    return output_list


# This functions takes two lists as parameters
# and returns a new list containing both.
def combinde_list(list_a, list_b):
    list_c = list_a
    for element in list_b[:]:
        index = 0
        extracted_list = list_b.pop(index)
        index = index + 1
        list_c.append(extracted_list)
    return list_c


# This function takes a list and a string as parameters
# and scrables them together. then it returns a new list.
def scramble_list(list_input, list_string):
    list_input[1] = list_string
    list_input[2] = list_string
    list_input[3] = list_string
    return list_input


# This function takes a list as parameter and
# returns a list with every other element.
def every_other_element(list_input):
    list_output = []
    list_input_count = 1
    for element in list_input[::2]:
        list_output.append(element)
    return list_output


# This function takes a list as parameter and
# returns a list with every other element.
def every_other_element(list_input):
    list_output = []
    list_input_count = 1
    for element in list_input:
        list_input_count = list_input_count + 1
        if list_input_count % 2 == 0:
            list_output.append(element)
    return list_output
