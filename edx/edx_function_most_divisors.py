# A function that accepts a list of integers and returns the integer that has the most divisors.
def find_integer_with_most_divisors(input_list):
    compare_list = []
    for element in input_list:
        count = 1
        element_count = 0
        while count <= element:
            if element % count == 0:
                element_count += 1
            count += 1
        compare_list.append(element_count)
        count = 0
        element_count = 0
    return input_list.pop(compare_list.index(max(compare_list)))
